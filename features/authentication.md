# Authentication

**Feature IDs:** F000005, F000007, F000020, F000023, F000047. See the [Feature register](feature-register.md).

## User story

As a visitor, I want to create an account, sign in securely, keep my session across normal navigation, sign out, and recover access if I forget my password, so that my learning data is private and available when I return.

## Expected behavior

### Registration

- The visitor can submit username, email, password, and password confirmation.
- Required fields and password mismatch are rejected before a successful account is created.
- Duplicate email or username is rejected with visible feedback.
- Successful registration leads the user to login rather than silently authenticating them.
- The backend creates the user and profile and creates the default `Other` section.

### Login and session

- Empty or invalid credentials show validation or authentication feedback.
- A successful login requests `/user/token/`, stores the refresh token and user identity, and navigates to `/dashboard`.
- Protected routes redirect unauthenticated visitors to login.
- The merged `develop` implementation stores a refresh token for later token refresh. A browser test checks that the session survives a reload immediately after login (see [Tests](#tests)). Restoring the session when the access token has expired or is missing is not covered and is what FE #57 addresses.
- As of 2026-11-26, [FE #57](https://github.com/LanguageAppSpace/language-app-frontend/pull/57) is open and proposes restoring a missing in-memory access token before protected requests, deduplicating concurrent refresh requests, and distinguishing public auth endpoints. It is not yet merged behavior.
- Logout clears local credentials, returns the user to the public flow, and prevents back-navigation into protected content.

### Password recovery

- A visitor can request a reset token using an email address.
- The reset token can be validated before a new password is submitted.
- Invalid tokens and mismatched new passwords are rejected.

## Implementation trace

- Frontend routes: `/register`, `/login`, `/forgot-password`, `/reset-password`.
- Frontend components: `language-app-frontend/src/Register/`, `src/Login/`, `src/ForgotPassword/`, `src/ResetPassword/`, and `src/routes/`.
- Frontend API: `src/redux/auth/authApiSlice.ts`.
- Backend routes: `backend-learning-platform/backend/user/urls.py`.
- Backend model: `backend-learning-platform/backend/user/models.py`.
- JWT and CORS planning card: Trello card `BE - Security : JWT token and CORS restrictions`.

## Tests

> **Note:** Test file paths below belong to the pre-migration test workspace. They are not available in [language-app-tests](https://github.com/LanguageAppSpace/language-app-tests) yet, and not all of them are committed anywhere. They record existing coverage; they are not runnable commands.
>
> Test instructions: pending migration to language-app-tests

This section lists what each test checks, not whether it currently passes. Check the latest report before relying on a result.

Backend API tests:

- `test/backend_tests/integration/test_user_auth_api.py` covers registration (user and profile created, mismatched passwords, duplicate email) and login (tokens returned, invalid password rejected).
- `test/backend_tests/integration/test_user_edge_cases.py` covers password-reset confirmation with an invalid token or mismatched passwords, and password change with a wrong old password.

Browser tests:

- `test/frontend_tests/run_register_suite.py` and `test/frontend_tests/run_login_suite.py` run the registration and login suites. Test instructions: pending migration to language-app-tests
- `test/frontend_tests/system/test_register_then_login.py` registers an account and signs in with it.
- `test/frontend_tests/test_register_duplicate_email.py` checks that registering with an existing email is rejected. It has not been moved into a category folder yet.
- `test/frontend_tests/system/test_dashboard_redirect_unauthenticated.py` checks that opening the dashboard without a session redirects to login.
- `test/frontend_tests/system/test_dashboard_logout_flow.py` checks that logout clears the refresh token and returns to the home page.
- `test/frontend_tests/system/test_dashboard_back_after_logout.py` checks that the browser Back button does not reopen the dashboard after logout.
- `test/frontend_tests/system/test_dashboard_cross_tab_session.py` checks that a signed-in session is available in a second tab.
- `test/frontend_tests/system/test_dashboard_refresh_preserves_session.py` reloads the dashboard right after login and expects the session to survive. It passed in the 2026-10-25 run (local report, not published). Because it reloads immediately, it does not exercise an expired or missing access token, or concurrent refreshes.
- `test/frontend_tests/acceptance/test_dashboard_corrupted_token.py` is an exploratory script. It records evidence for a corrupted or missing refresh token and is not a pass/fail acceptance test.

Account deactivation tests are listed in [Account and progress](account-and-progress.md#tests).

## Remaining checks

Add browser coverage for the complete password-reset journey, token refresh after the access token expires, and concurrent 401 responses. If FE #57 is merged, update this page from pending to implemented and verify that public registration, login, and password-reset requests are not blocked by the new auth guard.

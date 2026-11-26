# Account and Progress

**Feature IDs:** F000006, F000035, F000040, F000042. See the [Feature register](feature-register.md).

## User story

As a learner, I want to manage my profile and credentials and see meaningful progress, so that the application reflects my identity and motivates regular study.

## Expected behavior

### Profile and password

- An authenticated user can view and update first name, last name, photo, and birthdate.
- Profile photo validation rejects files larger than 2 MB.
- A user can change their password only with the correct old password and matching new passwords.
- A failed update shows an error and does not claim success.

### Deactivation

- A user can start account deactivation from settings.
- The action must require an explicit confirmation before it is submitted.
- On confirmation, the frontend submits `POST /user/deactivate-account/` with the active refresh token so the backend can deactivate the account and blacklist that token.
- After a successful response, the frontend clears all locally stored authentication state and redirects to the public landing page; the deactivated user must not remain signed in.
- Protected routes are inaccessible after deactivation, and attempting to open one redirects to login.
- If the request fails, the account remains signed in and an error notification is shown; the UI must not claim success.
- Browser tests that create disposable authenticated users deactivate those accounts during `close_session()` teardown. A test that explicitly tests deactivation marks its account as already deactivated to avoid repeating the request.

### Streak and lesson progress

- The dashboard displays the current streak.
- The first activity initializes the streak.
- Activity on the following day increments it.
- A gap resets it according to backend rules.
- Repeating an update on the same day does not increment it twice.
- Lesson progress is calculated from learned phrase pairs and can be reset.

## Implementation trace

- Frontend route/component: `/user-settings`, `language-app-frontend/src/Profile/UserSettings.tsx`.
- Frontend API and auth state: `src/redux/userSettings/userSettingsApiSlice.ts`, `src/redux/auth/authApiSlice.ts`, and `src/redux/auth/authSlice.ts`.
- Backend routes: `backend-learning-platform/backend/user/urls.py`.
- Backend behavior: `DeactivateAccountView` sets `is_active=False` and blacklists the submitted refresh token when present.
- Backend models: `backend-learning-platform/backend/user/models.py` and `backend/flashcards/models.py`.

## Tests

> **Note:** Test file paths below belong to the pre-migration test workspace. They are not available in [language-app-tests](https://github.com/LanguageAppSpace/language-app-tests) yet, and not all of them are committed anywhere. They record existing coverage; they are not runnable commands.
>
> Test instructions: pending migration to language-app-tests

This section lists what each test checks, not whether it currently passes. Check the latest report before relying on a result.

Backend API tests:

- `test/backend_tests/integration/test_user_streak_api.py` covers initialization, consecutive days, gaps, and same-day updates.
- `test/backend_tests/integration/test_user_streak_days_in_a_row.py` covers longer runs, month, year, and leap-day boundaries, per-user isolation, and unauthenticated requests.
- `test/backend_tests/integration/test_user_streak_risks.py` covers the risks recorded in the F000040 QA findings: the value read after a missed day, the configured time zone around midnight UTC, overlapping updates, and a `last_active` date in the future.
- `test/backend_tests/integration/test_user_edge_cases.py` covers a wrong old password on password change and a missing profile (HTTP 404).

Browser tests:

- `test/frontend_tests/system/test_dashboard_streak_text.py` verifies the dashboard streak text.
- `test/frontend_tests/acceptance/test_dashboard_streak_days_in_a_row.py` checks the streak for a new user and after a same-day reload, the update-then-read request order, and failure handling: a failed update, a failed read, and a missing streak field must not show `NaN`, `undefined`, or `null`.
- `test/frontend_tests/system/test_dashboard_settings_navigation.py` verifies navigation to settings.
- `test/frontend_tests/acceptance/test_user_panel_profile_form.py` covers the Update Profile form: fields, required-field validation, name and birthday persistence, birthday edge values, photo upload (PNG, WEBP, unsupported type, fake image, switching between URL and file), backend failure and offline states, several layout widths, and double submit.
- `test/frontend_tests/acceptance/test_profile_photo_url.py` covers an invalid photo URL, the preview for a valid URL, and saving a URL photo.
- `test/frontend_tests/acceptance/test_user_panel_profile_names_not_saved.py` reproduces a reported defect: saving the profile stores the birthday but not the first and last name, and the form does not show saved values after reload. It fails while that defect exists.
- `test/frontend_tests/system/test_deactivation_confirmation_dialog.py` verifies the confirmation dialog: title and warning text, Cancel sends no request, and Deactivate returns HTTP 200 and shows a success notification.
- `test/frontend_tests/acceptance/test_deactivation_logs_out_and_revokes_session.py` verifies what happens after confirmed deactivation: redirect to the landing page, cleared credentials, protected routes blocked in the current tab and in a previously open page, the refresh token rejected, and the access token rejected by the protected API.
- `test/frontend_tests/dashboard_test_utils.py` owns the reusable disposable-account teardown used by tests that call `create_logged_in_user()`.

## Remaining checks

Add browser coverage for password change; only the backend wrong-old-password case is tested. The backend rejects profile photos larger than 2 MB, but no test uploads an oversized file. Confirm whether the Miro design expects a locally uploaded photo, a URL, or both; the current form accepts both. The current frontend contract uses a `photo` field while the backend model uses an image field.

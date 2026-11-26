# Testing

This page records how LanguageApp is tested today and which tests are waiting to move to [language-app-tests](https://github.com/LanguageAppSpace/language-app-tests). Most browser tests have not been migrated yet.

Test instructions: pending migration to language-app-tests

## Where tests live (as of 2026-11-26)

| Location | What it contains | Status |
| --- | --- | --- |
| [Backend repository](https://github.com/LanguageAppSpace/backend-learning-platform) | Django tests in `backend/flashcards/tests.py` (25 test methods) and `backend/user/tests.py` (20) at revision `fd93263`. CI runs `python manage.py test --pattern="test*.py"` from `backend/` with `DJANGO_ENV=ci` (in-memory SQLite) on Python 3.10 for pushes and pull requests to `main`. | Committed and run by CI |
| [Frontend repository](https://github.com/LanguageAppSpace/language-app-frontend) | No test files and no test script at revision `21a533e`. CI runs `npm audit`, a TypeScript check and ESLint. | No automated tests |
| Pre-migration test workspace | Playwright browser tests, a Django-based backend runner, branch orchestration and generated reports. | Not published. Some files are not committed anywhere. |
| [language-app-tests](https://github.com/LanguageAppSpace/language-app-tests) | The intended home for the shared test suites. | No published content yet |

Test file paths in this documentation (for example `test/frontend_tests/...`) refer to the pre-migration test workspace. They are not available in language-app-tests, and the sections below describe that workspace as it was used. Treat them as a record of existing coverage, not as instructions you can run from a fresh clone. This page will be updated when the migration is complete.

Feature pages use this test vocabulary:

- **Unit/integration**: backend Django tests or focused frontend tests around a component/API slice.
- **Journey**: a multi-step browser scenario crossing several screens.
- **Regression**: a test added for a previously failing behavior.
- **Gap**: behavior described by the product but not currently covered by an executable test.

## Which environment the tests use

> **Warning:** Unless you configure them, the pre-migration browser tests run against the **shared staging site**, which is the harness default. Many of them register disposable accounts, create sections and lessons, and deactivate the accounts afterwards, so an unconfigured run writes data to shared staging.

Three settings decide where test traffic goes:

| Variable | Read by | Decides | Default when unset |
| --- | --- | --- | --- |
| `LANGUAGEAPP_BASE_URL` | browser tests (`test/frontend_tests/config.py`) | which frontend the tests open | shared staging |
| `LANGUAGEAPP_API_URL` | browser tests that also call the API directly | which backend those direct API calls use | `http://127.0.0.1:8001` if `LANGUAGEAPP_BASE_URL` contains `127.0.0.1`, otherwise a remote backend. Some profile tests always default to `http://127.0.0.1:8001`. |
| `VITE_API` | the frontend application | which backend the frontend calls | none in a fresh clone; set it as described in [Getting started](getting-started.md) |

To run browser tests against your own machine:

1. Start a local stack, for example [Isolated local staging](local-staging.md). It serves the frontend at `http://127.0.0.1:5173` and the API at `http://127.0.0.1:8001`.
2. In the terminal where you run the tests, point them at it. Use `127.0.0.1`, not `localhost`: tests that call the API directly only switch to the local API when the base URL contains `127.0.0.1`.

   ```powershell
   $env:LANGUAGEAPP_BASE_URL = "http://127.0.0.1:5173"
   $env:LANGUAGEAPP_API_URL = "http://127.0.0.1:8001"
   ```

3. Run the test or suite from the same terminal.

Setting these variables does not change which API a running frontend calls; `VITE_API` is fixed when the frontend starts. Confirm the API destination as described in [Getting started](getting-started.md) before running tests that write data.

## Backend tests

The backend repository's own tests are the committed ones. To run them the way CI does, set `DJANGO_ENV=ci` and a secret key, then run `python manage.py test --pattern="test*.py"` from the backend's `backend` directory after installing `backend/requirements.txt`. The [backend README](https://github.com/LanguageAppSpace/backend-learning-platform/blob/main/README.md) also describes running tests inside the development container; that command has not been verified here.

The pre-migration workspace has its own backend runner, `test/backend_tests/run_backend_suite.py`, which selects Django test cases by name and runs them from a local backend checkout with `DJANGO_ENV=ci`. Its case list has not been verified against the backend repository's committed tests, so use the backend repository's own command when you need an authoritative backend result.

## Pre-migration branch runner

`test/run_branch_test.py` checks out selected frontend and backend branches, runs suites, restores the original branches, and writes reports. What it actually tests differs between frontend and backend:

- **Backend:** `--run-backend` runs `run_backend_suite.py` against the backend branch that is checked out.
- **Frontend:** the runner checks out the frontend branch but does **not** build or start it. Browser suites test whatever site `LANGUAGEAPP_BASE_URL` points to, which is shared staging by default. A passing frontend suite therefore says nothing about the checked-out branch unless that branch is the one being served at `LANGUAGEAPP_BASE_URL`.

To test a frontend branch, check it out yourself, serve it locally (for example with the local staging stack), set the variables above, and then run the suite.

Examples from the pre-migration workspace (set the variables first to avoid shared staging):

```powershell
python test/run_branch_test.py --frontend-branch la-119 --frontend-suite smoke
python test/run_branch_test.py --frontend-branch la-119 --backend-branch la-128 --frontend-suite dashboard --run-backend
python test/run_branch_test.py --frontend-branches develop --backend-branches main --frontend-suite all --run-backend
```

The runner normally refuses to switch a repository with uncommitted changes. Commit or stash changes first, or use `--allow-dirty` only when you understand the consequences. As of 2026-11-26, the smoke, login, register, dashboard and dashboard-journey runners list test paths from before the test reorganization, and most of those paths no longer exist (for example 28 of 28 in the smoke runner). Only the landing runner lists paths that all exist, so a suite failure may mean a moved path rather than a product defect.

## Clean up shared staging

If tests have run against shared staging, two scripts in `test/frontend_tests/acceptance/` remove leftover test data. Both act on the site that `LANGUAGEAPP_BASE_URL` points to and write evidence to the folder you pass as the first argument.

- `cleanup_historical_staging_test_accounts.py <artifacts-folder>` searches files under `reports/` for disposable usernames (`john_doe_` followed by digits), signs in to each account, and deactivates it. It uses `STAGING_TEST_PASSWORD` when set, otherwise the harness's default test password.
- `cleanup_staging_user_lessons.py <artifacts-folder>` signs in as `STAGING_TEST_USERNAME` with `STAGING_TEST_PASSWORD` and deletes every lesson in that account's default `Other` section.

Both scripts are destructive and cannot be undone. Check `LANGUAGEAPP_BASE_URL` and the target account before running them, and never put real credentials in a committed file.

## Reports

Branch test runs produce timestamped reports and visual artifacts. Reports are local artifacts: they are not published, and this repository ignores `reports/`. Pages that cite a "local report" refer to evidence you cannot open from GitHub.

When reporting a failure, include:

- the frontend and backend branch names
- the suite name
- the command used
- the generated report path
- the first failing test and its error output

## Adding a test

Place a test beside the suite or component it exercises. Keep browser tests focused on user-visible behavior and backend tests focused on API, model, and authentication behavior. Until the migration is complete, state in your pull request whether a new test file is committed and where. Update this page when a new suite or required service is introduced.

## Feature traceability

Each feature specification should identify:

1. the user story and acceptance criteria
2. the frontend route/component and backend endpoint/model
3. the automated tests that verify the acceptance criteria
4. manual checks for behavior not yet automated
5. known gaps or planned extensions from Trello/Miro

## Pre-migration workspace history

The workspace that holds the browser tests is not part of the product and is not listed in the release history. Its committed history is short:

| Date | Change |
| --- | --- |
| 2026-07-15 | `init_shared_test_harness`: shared browser and backend test harness. |
| 2026-08-20 | Dashboard tests and workflow updated. |

Tests for card 131 (vocabulary button), cards 101 and 102 (study streak, frontend and backend), and dashboard section and lesson management were added after these commits. At the time of writing they were not all committed.

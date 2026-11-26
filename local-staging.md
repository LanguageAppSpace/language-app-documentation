# Isolated local staging environment

> **Status:** This setup belongs to the pre-migration test workspace. The Compose file it uses, `docker-compose.local-staging.yml`, is not published in any LanguageAppSpace repository as of 2026-11-26. It also expects the backend and frontend checkouts to be folders named `backend-learning-platform` and `language-app-frontend` next to the Compose file. The commands below are preserved for reference and will be updated when the file moves to [language-app-tests](https://github.com/LanguageAppSpace/language-app-tests).
>
> Test instructions: pending migration to language-app-tests

This setup runs the current backend code against a dedicated MySQL volume and serves the frontend through Vite in Docker. It does not contact the shared staging app or backend. The API and frontend are published only on loopback at `127.0.0.1:8001` and `127.0.0.1:5173` respectively.

## Requirements

- Docker Desktop with Docker Compose v2
- Node.js/npm installed
- Project Python virtual environment and Playwright browser dependencies for browser tests

## Start the local backend

From the folder that contains the Compose file, start the database, backend, and frontend with a distinct Compose project name:

```powershell
docker compose -p languageapp-local-staging -f docker-compose.local-staging.yml up --build -d
```

The first start builds the backend image, initializes the isolated MySQL database, applies Django migrations, installs the frontend dependencies in a dedicated named volume, and starts Vite. Check startup with:

```powershell
docker compose -p languageapp-local-staging -f docker-compose.local-staging.yml ps
docker compose -p languageapp-local-staging -f docker-compose.local-staging.yml logs -f backend
```

Open the local frontend at `http://127.0.0.1:5173`; it is configured to call the local API at `http://127.0.0.1:8001`. New registrations create their own default “Other” section.

## Run browser tests locally

In a second PowerShell terminal, set the test base URL before launching a browser test. For example, to run the account-deactivation confirmation test from the pre-migration workspace:

```powershell
$env:LANGUAGEAPP_BASE_URL = "http://127.0.0.1:5173"
& ".\.venv\Scripts\python.exe" test\frontend_tests\run_instrumented_test.py test\frontend_tests\system\test_deactivation_confirmation_dialog.py reports\local_deactivation_confirmation
```

The default test URL remains the shared staging site when `LANGUAGEAPP_BASE_URL` is unset. Set it explicitly to localhost for local runs to avoid touching staging. The test registers and deactivates only its disposable local account. See [Testing](testing.md) for the variables and their limits.

## Stop and reset

Stop containers but keep the local database volume:

```powershell
docker compose -p languageapp-local-staging -f docker-compose.local-staging.yml down
```

Permanently remove the local database and all local test accounts/data:

```powershell
docker compose -p languageapp-local-staging -f docker-compose.local-staging.yml down -v
```

This Compose project uses uniquely named database and frontend dependency volumes and does not mount or modify the regular backend Compose database volume.

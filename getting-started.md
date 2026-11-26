# Getting started

To read or edit these guides, you only need Markdown. To run the app, clone the
frontend and backend separately; neither expects to run inside this repository.

## Prerequisites

- Git.
- Node.js and npm for the frontend. The frontend CI uses Node.js 18.
- Docker with Docker Compose for the backend. You do not need a local Python installation when you use Docker; the backend image uses Python 3.11.

## Steps

1. **Start the backend.** Follow the [backend README](https://github.com/LanguageAppSpace/backend-learning-platform/blob/main/README.md) to configure local database and Django settings. From the backend root, run `docker compose -f docker-compose.dev.yml up --build`. Check that `http://127.0.0.1:8000/swagger/` opens.
2. **Select the local API.** In the frontend root, set `VITE_API=http://127.0.0.1:8000` in `.env.local`. Local environment files are ignored by Git: a fresh clone does not inherit another developer's API address.
3. **Start the frontend.** From the frontend root, run `npm install`, then `npm run dev` (see the [frontend README](https://github.com/LanguageAppSpace/language-app-frontend/blob/develop/README.md)). Open the URL Vite prints. Restart Vite after changing `VITE_API`.

### Backend environment file

The backend reads its settings from a `.env` file in the backend root that is not committed. The [backend README](https://github.com/LanguageAppSpace/backend-learning-platform/blob/main/README.md) lists the variable names under Environment Variables. The repository does not currently contain an `.env.example` template, so create `.env` yourself using those names. The development Compose file is named `docker-compose.dev.yml`.

### Frontend commands

Run these from the frontend root: `npm run dev` (Vite development server), `npm run build` (TypeScript check, then production build), `npm run lint` (ESLint), `npm run preview` (serve the production build) and `npm run format` (Prettier).

### Environment variables

Names only; never commit values.

| Variable | Read by | Purpose |
| --- | --- | --- |
| `VITE_API` | frontend | Base URL of the backend API. It is read when Vite starts or the app is built, and a fresh clone has no value. |
| `DJANGO_ENV` | backend settings and scripts | Selects `ci`, `development` or the production configuration. The Compose files set it. |
| `DJANGO_SECRET_KEY` | backend Compose files | Django secret key, passed to the container as `SECRET_KEY`. |
| `DEBUG` | backend settings | Debug mode; off unless set to `1`, `true` or `yes`. |
| `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_ROOT_PASSWORD`, `DB_HOST`, `DB_PORT` | backend Compose files and settings | MySQL connection and the database container's credentials. |
| `PORT` | backend start script | Port Gunicorn binds to outside development; defaults to 8080. |
| `EMAIL_HOST`, `EMAIL_PORT`, `EMAIL_USE_TLS`, `EMAIL_HOST_USER`, `EMAIL_HOST_PASSWORD`, `DEFAULT_FROM_EMAIL` | backend settings | SMTP settings for outgoing email such as password reset. |

Variables for the pre-migration browser tests are described in [Testing](testing.md).

## Verify the API destination in Chrome

1. Open the local frontend's sign-in page. Press `F12` to open DevTools, select **Network**, then **Fetch/XHR**.
2. In the Network panel's throttling menu, select **Offline**. Without reloading the page, submit the form with a made-up email address and password. Chrome will record the attempted request without sending it.
3. Click the failed sign-in request. Under **Headers** > **General**, read **Request URL**. For the setup above, it should start with `http://127.0.0.1:8000/`. This checks the destination, not whether the backend is running.
4. Restore **No throttling**. If the URL is different or no request appeared, do not sign in or register online. Recheck `VITE_API`, restart Vite and repeat the check.

## Before running browser tests

**Warning:** The existing browser harness defaults to shared staging when
`LANGUAGEAPP_BASE_URL` is unset. Some suites create accounts and lessons.
That variable selects the site the browser opens, not its API. A local frontend
URL alone does not guarantee that the app or tests send writes to a local API.
Confirm both destinations before running a suite. See [Testing](testing.md) for the harness variables and the pre-migration status.

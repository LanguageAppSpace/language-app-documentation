# Getting started

To read or edit these guides, you only need Markdown. To run the app, clone the
frontend and backend separately; neither expects to run inside this repository.

1. **Start the backend.** Follow the [backend README](https://github.com/LanguageAppSpace/backend-learning-platform/blob/main/README.md) to configure local database and Django settings. From the backend root, run `docker compose -f docker-compose.dev.yml up --build`. Check that `http://127.0.0.1:8000/swagger/` opens.
2. **Select the local API.** In the frontend root, set `VITE_API=http://127.0.0.1:8000` in `.env.local`. Local environment files are ignored by Git: a fresh clone does not inherit another developer's API address.
3. **Start the frontend.** From the frontend root, run `npm install`, then `npm run dev` (see the [frontend README](https://github.com/LanguageAppSpace/language-app-frontend/blob/develop/README.md)). Open the URL Vite prints. Restart Vite after changing `VITE_API`.

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
Confirm both destinations before running a suite. Test commands will follow in PR 3.

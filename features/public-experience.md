# Public Experience

**Feature IDs:** F000002, F000012, F000021, F000022, F000024, F000025, F000026, F000030, F000033. See the [Feature register](feature-register.md).

## User story

As a prospective learner, I want to understand the application and find clear paths to register or sign in, so that I can decide whether to start learning without needing an existing session.

## Expected behavior

- `/home` presents the product value and clear registration/login entry points.
- Navigation works on desktop and mobile, including the hamburger menu.
- About Us, Contact, Support, Privacy Policy, and Learn More pages are reachable through their public routes.
- Public pages do not require authentication.
- Authenticated-only pages are not exposed through public navigation.
- Invalid routes render the 404 page.
- Footer and social links remain usable and point to the intended destinations.

## Implementation trace

- Routes and layouts: `language-app-frontend/src/App.tsx`, `src/layouts/Public/`, and `src/LandingPage/`.
- Public page components: `src/pages/`, `src/LandingPage/AboutUs.tsx`, and `src/LandingPage/Contact.tsx` where applicable.
- Route constants: `src/config/route.config.ts`.

## Tests

> **Note:** Test file paths below belong to the pre-migration test workspace. They are not available in [language-app-tests](https://github.com/LanguageAppSpace/language-app-tests) yet, and not all of them are committed anywhere. They record existing coverage; they are not runnable commands.
>
> Test instructions: pending migration to language-app-tests

`test/frontend_tests/run_landing_suite.py` covers the landing page, navigation, hero, feature cards, newsletter, footer links, social links, and public-page entry points. The suite should be treated as the executable acceptance layer for the public experience.

## Remaining checks

Verify content and visual relationships against the private Miro board after design changes. Add a direct 404 test and responsive checks for every public page, not only the landing page.

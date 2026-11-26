# Dashboard and Organization

**Feature IDs:** F000011, F000013, F000019, F000028, F000044, F000045, F000048. See the [Feature register](feature-register.md).

## User story

As an authenticated learner, I want a dashboard that shows my activity and lets me organize lessons into sections, so that I can quickly resume learning and keep related vocabulary together.

## Expected behavior

### Dashboard

- An authenticated user can open `/dashboard` and sees their username and current streak.
- An unauthenticated user is redirected away from the dashboard.
- The dashboard exposes navigation to settings, logout, section creation, and standalone lesson creation.
- Loading states and success/error notifications are visible while data is being fetched or changed.
- A user with no sections sees an empty state and a create-section call to action.
- The default `Other` section can contain lessons that have not been organized elsewhere.

### Sections

- A user can create a section with a title, optional description, and selected color.
- A title and color are required; invalid input remains in the modal with feedback.
- A user can open a section, edit it, or delete it after confirmation.
- Sections display their lesson count and provide an add-lesson action.
- A user can open a section with no lessons and sees a lesson empty state.
- Section data is scoped to the authenticated user.

### Lesson list and progress

- A section lists its lessons, phrase count, and progress bar.
- A lesson can be opened to choose a learning mode.
- A user can edit, delete, or reset lesson progress from its card.

## Implementation trace

- Frontend routes: `/dashboard`, `/section/:sectionId`.
- Frontend components: `src/UserDashboard/Main.tsx`, `src/UserDashboard/Sections/`, and `src/UserDashboard/Sections/SectionView/`.
- Frontend API: `src/redux/sections/sectionsApiSlice.ts` and `src/redux/lessons/lessonsApiSlice.ts`.
- Backend model: `backend-learning-platform/backend/flashcards/models.py`.
- Backend routes: `backend-learning-platform/backend/flashcards/urls.py`.
- Streak API: `backend-learning-platform/backend/user/urls.py`.

## Tests

> **Note:** Test file paths below belong to the pre-migration test workspace. They are not available in [language-app-tests](https://github.com/LanguageAppSpace/language-app-tests) yet, and not all of them are committed anywhere. They record existing coverage; they are not runnable commands.
>
> Test instructions: pending migration to language-app-tests

This section lists what each test checks, not whether it currently passes. Check the latest report before relying on a result.

Suites:

- `test/frontend_tests/run_dashboard_suite.py` and `test/frontend_tests/run_dashboard_journey_suite.py`. Test instructions: pending migration to language-app-tests

Browser tests:

- Journey steps 01 to 05 in `test/frontend_tests/acceptance/`: `test_dashboard_journey_01_dashboard_visible.py`, `test_dashboard_journey_02_open_section_modal.py`, `test_dashboard_journey_03_section_validation.py`, `test_dashboard_journey_04_create_section.py`, and `test_dashboard_journey_05_open_new_section_empty_state.py`. Steps 06 to 10 cover lesson creation; see [Lesson authoring](lesson-authoring.md#tests).
- `test/frontend_tests/acceptance/test_dashboard_section_lesson_management.py` covers section create, edit (prefill, cancel, save, required title, Escape), and delete with confirmation; lesson counts; the `Other` section's edit-only actions; multiple lessons in a section; lesson reset progress; lesson delete with confirmation; lesson edit navigation; and a second user not seeing the first user's sections. One check is marked as an expected failure: a long title without spaces pushes the card actions out of the card, which is the problem FE #60 addresses.
- `test/frontend_tests/acceptance/test_dashboard_default_other_section_protected.py` checks that the `Other` section has no delete action, a user-created section does, and `Other` is still present after reload.
- `test/frontend_tests/acceptance/test_dashboard_exploratory.py` automates exploratory checks: special characters and very long input, double submit, and backend failures (500 and offline) on the section list and on create.
- `test/frontend_tests/system/` contains focused dashboard checks: authenticated access, redirect when unauthenticated, greeting, logo, menu, logout, mobile layout, the empty `Other` section, the success toast, the create-section and create-lesson entry points, and settings navigation.
- Evidence scripts that record behavior rather than pass or fail: `test/frontend_tests/acceptance/test_dashboard_double_click_save.py` (how many sections a double click on Save creates) and `test/frontend_tests/acceptance/test_dashboard_sections_over_page_limit.py` (sections beyond the API page size of 9 are not shown).

Backend tests:

- `test/backend_tests/run_backend_suite.py` runs section and lesson view-set cases, including protection of the default `Other` section.
- Streak tests are listed in [Account and progress](account-and-progress.md#tests).

## Remaining checks

Add browser or API coverage for authorization between users beyond the dashboard list, for example opening another user's section or lesson by URL. Add a regression test for the Trello-reported section color issue (card 118) when that behavior is changed. Decide whether the double-click and page-size evidence scripts should become pass/fail tests once the expected behavior is agreed.

# Lesson Authoring

**Feature IDs:** F000008, F000044, F000045, F000049, F000050, F000051. See the [Feature register](feature-register.md).

## User story

As a learner, I want to create and maintain lessons made of phrase pairs, optionally assign them to a section, and correct individual pairs later, so that my study material stays useful over time.

## Expected behavior

### Create

- The user can start from the dashboard or a section.
- The form accepts a lesson title, description, and one or more phrase/translation pairs.
- The user can add vocabulary rows before submitting.
- A lesson created inside a section is assigned to that section.
- A standalone lesson is handled according to the backend's section assignment rules, including the default `Other` section where applicable.
- Successful creation returns the user to the relevant lesson/section view and refreshes the lesson list.
- The backend accepts an optional `tags` list. Names are trimmed, case-folded, deduplicated, and scoped to the authenticated user.
- A lesson can be marked as a language lesson. Language lessons require non-empty `source_language` and `target_language`, and the values must differ.

### List and find

- Lesson search by name and sorting by creation date are implemented in the frontend.
- The backend returns `created_at`, `is_language_lesson`, `source_language`, `target_language`, and normalized tag names with lessons.
- `GET /flashcards/lessons/?tag=name` filters by one tag. Multiple `tag` query parameters are combined as repeated intersections.
- Frontend tag and language authoring/filtering controls are not yet merged into `develop`.

### Edit

- The user can open `/section/:sectionId/edit-lesson/:lessonId`.
- Existing lesson fields and phrase pairs are loaded into the form.
- The user can update lesson metadata and phrase pairs.
- A phrase pair can be updated or deleted without changing unrelated pairs.
- A failed request keeps the user informed and does not present stale data as saved.
- Updating language fields uses the same language-lesson validation as creation.
- Supplying tags on update adds those tags to the lesson. Explicit tag removal semantics still need product/API definition.

### Delete and progress reset

- Deleting a lesson requires confirmation and removes it from its section.
- Resetting progress marks the lesson's phrase pairs as unlearned.
- The progress bar reflects the calculated learned-pair percentage after refresh.

## Implementation trace

- Frontend routes: `/create-lesson`, `/section/:sectionId/create-lesson`, `/section/:sectionId/edit-lesson/:lessonId`.
- Frontend component: `language-app-frontend/src/Lessons/CreateEditLesson.tsx`.
- Frontend API: `src/redux/lessons/lessonsApiSlice.ts`.
- Backend routes: `backend-learning-platform/backend/flashcards/urls.py`.
- Backend model: `backend-learning-platform/backend/flashcards/models.py`.
- Data contracts: `language-app-frontend/src/interface/index.ts`.

## Tests

> **Note:** Test file paths below belong to the pre-migration test workspace. They are not available in [language-app-tests](https://github.com/LanguageAppSpace/language-app-tests) yet, and not all of them are committed anywhere. They record existing coverage; they are not runnable commands.
>
> Test instructions: pending migration to language-app-tests

This section lists what each test checks, not whether it currently passes. Check the latest report before relying on a result.

Browser tests:

- `test/frontend_tests/run_dashboard_journey_suite.py`, steps 06 to 10 (`test/frontend_tests/acceptance/test_dashboard_journey_06_create_lesson_navigation.py` to `test_dashboard_journey_10_open_created_lesson_dialog.py`): navigation, form fields, adding a vocabulary row, submit, and opening the created lesson.
- `test/frontend_tests/acceptance/test_search_lessons_by_name.py` covers case-insensitive substring search, the no-match message, and clearing the search.
- `test/frontend_tests/acceptance/test_lesson_sort_by_creation_date.py` checks that Cancel in the sort dialog keeps the order and that applying "Newest first" reorders the lessons.
- `test/frontend_tests/acceptance/test_cancel_create_edit_forms.py` checks that Cancel on the create and edit forms sends no create or update request.
- `test/frontend_tests/acceptance/test_dashboard_section_lesson_management.py` covers lesson delete with confirmation, reset progress, and that the edit icon opens the edit form. See [Dashboard and organization](dashboard-and-organization.md#tests).
- `test/frontend_tests/acceptance/test_add_vocabulary_existing_default_lesson.py` checks that vocabulary can be added to an existing lesson in the `Other` section.
- `test/frontend_tests/acceptance/test_add_vocabulary_button_not_hidden_by_footer.py` checks that the "Add new vocabulary" button is not covered by the bottom bar (card 131).
- `test/frontend_tests/acceptance/test_create_default_lesson_once.py` checks that one save creates exactly one lesson in the `Other` section.
- `test/frontend_tests/acceptance/test_staging_lesson_creation_regression_20.py` and `test_staging_lesson_creation_zero_one_phrase_20.py` are lesson-creation regression scripts written for shared staging, including lessons with zero or one phrase pair.

Backend tests:

- `test/backend_tests/run_backend_suite.py` lesson create, reload, list, detail, delete, progress, phrase-pair update, and phrase-pair delete cases.
- Backend `LessonViewSetTests` cover language-lesson creation, regular lessons, missing source/target, matching languages, updates, enabling/disabling language mode, and returned language fields.
- Tag behavior should be verified against BE #21; it is merged but is not represented in the shared backend runner's selected test cases.

## Remaining checks

Add focused browser tests for edit persistence (current tests only check that the edit form opens and that Cancel sends nothing), empty or malformed phrase pairs, duplicate lesson submissions, network failure while saving a lesson, combined search and sort, and backend tag and language payload compatibility. Add frontend controls and tests before describing tag filtering or language selection as a complete full-stack feature.

As of 2026-11-26, [FE #60](https://github.com/LanguageAppSpace/language-app-frontend/pull/60) is pending and wraps long section and lesson titles/descriptions without overflowing their cards. It must remain described as pending until merged into `develop`.

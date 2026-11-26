# Release History

This page traces what was delivered over time in the two application repositories. Feature IDs link to the [Feature register](features/feature-register.md), which holds the scope (FE, BE or FS), card, pull requests, and specification for each one.

## How releases are defined

Neither repository has Git tags or GitHub releases. The releases below (`R01` to `R11`) are **reconstructed milestones**: calendar periods that group everything merged into the main line (`develop` for the frontend, `main` for the backend) during the period. They are a reading aid, not published version numbers.

- A change belongs to the release that contains its merge date, or its commit date when there was no pull request.
- Bug fixes are listed with the card number of the bug when one exists. Dependency bumps by Dependabot are summarized, not listed.
- When real releases are introduced, tag both repositories (for example `v1.0.0`) and replace the period boundaries below with tag names. See [Contributing](contributing.md#releases-and-feature-ids).

Sources audited 2026-11-26: `git log` of `language-app-frontend` (298 commits, 2024-03-05 to 2026-10-22) and `backend-learning-platform` (127 commits, 2024-05-08 to 2026-11-26), the exported Trello board, and GitHub open pull requests.

## Overview

| Release | Period | Theme | Features delivered |
| --- | --- | --- | --- |
| [R01](#r01-2024-03-05-to-2024-05-31-project-start) | 2024-03-05 to 2024-05-31 | Project start | F000001 to F000007 |
| [R02](#r02-2024-06-01-to-2024-08-31-api-and-flashcards) | 2024-06-01 to 2024-08-31 | API and flashcards | F000008 to F000010, plus second halves of F000005 and F000006 |
| [R03](#r03-2024-09-01-to-2024-12-31-dashboard-and-lesson-form) | 2024-09-01 to 2024-12-31 | Dashboard and lesson form | F000011 to F000014, plus the frontend of F000008 |
| [R04](#r04-2025-01-01-to-2025-05-31-refactoring-and-hosting) | 2025-01-01 to 2025-05-31 | Refactoring and hosting | F000015 to F000018 |
| [R05](#r05-2025-06-01-to-2025-09-30-account-recovery-and-public-pages) | 2025-06-01 to 2025-09-30 | Account recovery and public pages | F000019 to F000027 |
| [R06](#r06-2025-10-01-to-2025-12-31-sections) | 2025-10-01 to 2025-12-31 | Sections | F000028 to F000031 |
| [R07](#r07-2026-01-01-to-2026-03-31-progress-and-quiz) | 2026-01-01 to 2026-03-31 | Progress and quiz | F000032 to F000035, plus frontends of F000010 and F000031 |
| [R08](#r08-2026-04-01-to-2026-05-31-streak-lesson-types-and-translations) | 2026-04-01 to 2026-05-31 | Streak, lesson types, translations | F000036 to F000041 |
| [R09](#r09-2026-06-01-to-2026-08-31-account-safety-and-search) | 2026-06-01 to 2026-08-31 | Account safety and search | F000042 to F000047 |
| [R10](#r10-2026-09-01-to-2026-10-22-photos-sorting-and-polish) | 2026-09-01 to 2026-10-22 | Photos, sorting, polish | F000048, F000049, plus frontends of F000035 and F000044 |
| [R11](#r11-2026-11-03-to-2026-11-26-lesson-metadata) | 2026-11-03 to 2026-11-26 | Lesson metadata | F000050, F000051 |

## R01: 2024-03-05 to 2024-05-31 Project start

Frontend and backend repositories were created separately.

**Features**

- F000001 (FE) Frontend foundation (Vite, React, TypeScript, MUI, Redux).
- F000002 (FE) Landing page: navigation, hero, features, about, testimonials.
- F000003 (BE) Docker setup.
- F000004 (BE) flake8 and first GitHub workflow.
- F000005 (FS) Backend user model, JWT registration and login (backend "Feature #1", 2024-05-10).
- F000006 (FS) Backend profile endpoint (same change).
- F000007 (FE) Registration and login screens with Firebase and Google sign-in (merged 2024-05-20).

## R02: 2024-06-01 to 2024-08-31 API and flashcards

**Features**

- F000008 (FS) Backend flashcards app: lessons and phrase pairs with CRUD API (2024-06-12).
- F000010 (FS) Backend progress: `is_learned` flag and rounded progress percent (2024-07-06).
- F000005 (FS) Frontend authenticates against the backend API (merged 2024-07-11).
- F000006 (FS) Frontend user settings page (merged 2024-08-27).
- F000007 (FE) Registration and login finished (Google sign-in merged 2024-06-11).
- F000009 (BE) Backend main page.
- F000004 (BE) Test workflow, pylint, Dependabot.

**Fixes**

- Backend BugFix #30 (2024-08-06): JWT authentication in user views. CSRF token correction.
- Backend BugFix #34 (2024-08-10): profile retrieval and update.

**Maintenance**: Dependabot upgrades of Python packages (June to September).

## R03: 2024-09-01 to 2024-12-31 Dashboard and lesson form

**Features**

- F000011 (BE) Lesson ownership and user statistics endpoint (2024-09-05).
- F000008 (FS) Frontend vocabulary inputs (2024-09-12), lesson form with edit (2024-11-18), delete flashcards (2024-12-04).
- F000012 (FE) Routing, public layout, and 404 page (merged 2024-09-16).
- F000013 (FE) Dashboard shell (merged 2024-10-08).
- F000014 (FE) Styling refactor to styled-components starts (2024-12-18).

## R04: 2025-01-01 to 2025-05-31 Refactoring and hosting

**Features**

- F000015 (BE) MySQL, production Docker Compose, domain, frontend URL whitelist (January to April 2025).
- F000014 (FE) Styling refactor completed: theme colors, sizes, breakpoints (to 2025-03-26).
- F000016 (FE) Frontend CI/CD and Netlify deploys.
- F000017 (FE) Prettier, ESLint fixes, README.
- F000018 (FE) Structure reorganization and separate login and register pages.
- F000002 (FE) "Features" section removed from the landing page (2025-04-10).

**Technical**: Firebase removed from the frontend (2025-02-18). The frontend now relies only on the backend API.

## R05: 2025-06-01 to 2025-09-30 Account recovery and public pages

**Features**

- F000023 (FS) Forgot password: backend 2025-08-11 and 2025-08-25, frontend 2025-08-27.
- F000019 (FE) User's lessons on the dashboard (2025-07-04).
- F000020 (FE) Auth pages layout, back button, friendly registration errors (2025-07-07).
- F000021 (FE) Privacy policy (2025-07-23).
- F000022 (FE) Navigation bar (2025-07-29 and 2025-09-04).
- F000024 (FE) Support page and FAQ (2025-08-13).
- F000025 (FE) "Join now" opens registration with the email prefilled (2025-08-27).
- F000026 (FE) About Us (2025-09-09).
- F000027 (FE) First flashcards learning page (2025-09-12).

**Fixes**

- Cards 78 and 79: duplicated values after updating a lesson (2025-06-23).

## R06: 2025-10-01 to 2025-12-31 Sections

**Features**

- F000028 (FS) Sections: default "Other" section (backend 2025-10-19), create sections (frontend 2025-12-02), section view with lessons and unassigned lessons (2025-12-10).
- F000031 (FS) Reset progress for lessons and sections: backend (2025-11-04). `BasicAuthentication` was removed in the same change.
- F000029 (FE) Browse and review modes (2025-10-20).
- F000030 (FE) Contact Us (2025-10-27).

**Fixes and technical**

- Card 82: left navigation hidden for signed-out users, duplicated sidebar fixed, authentication fix (2025-11-17).
- Backend replaced `TokenUser` with `CustomUser` and updated allowed hosts (2025-11-17).

## R07: 2026-01-01 to 2026-03-31 Progress and quiz

**Features**

- F000035 (FS) Backend profile photo upload (2026-03-24).
- F000031 (FS) Reset progress in the frontend (2026-02-23).
- F000010 (FS) Progress bar in the frontend (2026-02-25).
- F000032 (FE) Flashcard review animations (2026-01-27).
- F000033 (FE) Layout with maximum-width container (2026-02-16).
- F000034 (FE) Quiz lesson type (2026-03-24).

**Fixes**

- Card 95: settings text color (2026-02-05).
- Card 109: progress bar refreshed only after reload (2026-03-09).
- `VITE_API` missing in the build (2026-01-14).

## R08: 2026-04-01 to 2026-05-31 Streak, lesson types, and translations

**Features**

- F000040 (FS) Daily study streak: backend 2026-05-14, frontend 2026-05-30.
- F000037 (FE) Swipe flashcards on a phone (2026-05-05).
- F000038 (FE) Lesson summary view (2026-05-06).
- F000039 (FE) UI texts moved to translation files (2026-05-06).
- F000041 (FE) Matching pairs lesson type (2026-05-19).
- F000036 (BE) Deployment pipeline starts: SSH check (2026-05-05), deploy action (2026-05-06).
- F000004 (BE) GitHub workflows updated, ruff formatting, pre-commit (2026-04-20).

## R09: 2026-06-01 to 2026-08-31 Account safety and search

**Features**

- F000042 (FS) Account deactivation: backend blacklists the refresh token of an inactive user (2026-06-14); frontend logs out and redirects (2026-07-18) and asks for confirmation (2026-07-30).
- F000044 (FS) Backend lesson creation date (2026-07-06).
- F000043 (FE) Written answer lesson type (2026-06-17).
- F000045 (FE) Search lessons by name (2026-07-18).
- F000036 (BE) Migrations after deployment and secure proxy (2026-06-11).
- F000046 (BE) Spaced repetition fields and review endpoint (2026-08-12).
- F000047 (BE) Custom message when the email already exists (2026-08-12).

**Fixes**

- Card 131: "Add New Vocabulary" button visibility (2026-07-18). A browser test exists in the pre-migration test workspace: `test/frontend_tests/acceptance/test_add_vocabulary_button_not_hidden_by_footer.py`. QA could not reproduce the problem on the local stack at the tested viewports (local QA report, not published).

## R10: 2026-09-01 to 2026-10-22 Photos, sorting, and polish

**Features**

- F000035 (FS) Frontend profile photo upload and preview (2026-09-24).
- F000044 (FS) Sort lessons by creation date (2026-10-22).
- F000048 (FE) Default "Other" section cannot be deleted (2026-09-04).
- F000049 (FE) Cancel button on create and edit forms (2026-10-11).

**Fixes**

- F000046 (BE) Review endpoint returns the cards scheduled for review (2026-10-05).

## R11: 2026-11-03 to 2026-11-26 Lesson metadata

**Features**

- F000050 (BE) Lesson tags, user-scoped tag ownership, case-normalization, and repeated `tag` list filters (merged 2026-11-03 in BE #21).
- F000051 (BE) Language lessons with `is_language_lesson`, `source_language`, `target_language`, and validation (merged 2026-11-26 in BE #22).

**Pending at 2026-11-26** (open frontend pull requests; see the [live list](https://github.com/LanguageAppSpace/language-app-frontend/pulls) for current status)

- [FE #57](https://github.com/LanguageAppSpace/language-app-frontend/pull/57): session restoration and deduplicated token refresh.
- [FE #58](https://github.com/LanguageAppSpace/language-app-frontend/pull/58): section review banner and section-wide review route.
- [FE #59](https://github.com/LanguageAppSpace/language-app-frontend/pull/59): draft flashcard text-to-speech using temporary language codes.
- [FE #60](https://github.com/LanguageAppSpace/language-app-frontend/pull/60): wrapping for long section and lesson text.

## Known gaps in this history

- Releases are reconstructed, not published. There is no way to tell from Git which build was deployed to staging or production on a given date.
- Frontend pull requests merged before 2024-11 were opened in `karinazz/LanguageApp`. Their dates are the merge dates in that repository.
- Cards are matched to commits by the `la-<number>` branch names and commit messages. A few backend commits (for example the 2024 `Feature #n` commits) predate that convention and have no card number.

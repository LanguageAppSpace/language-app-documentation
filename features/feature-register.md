# Feature Register

This register gives every delivered feature a stable ID and links it to its planning card, pull requests, release, and specification page. It was first reconstructed from the full Git history of both application repositories on 2026-11-02 and last updated on 2026-11-26. It complements [Release history](../release-history.md).

## ID scheme

Every feature has one ID in a single sequence: `Fxxxxxx` (for example `F000040`). The **Scope** column tells who delivered it:

| Scope | Meaning |
| --- | --- |
| `FE` | Frontend only (`language-app-frontend`) |
| `BE` | Backend only (`backend-learning-platform`) |
| `FS` | Full-stack: one feature delivered by frontend and backend together |

Rules:

1. IDs are assigned in order of the earliest date a feature reached the main line (`develop` for the frontend, `main` for the backend). The initial numbering was done in that order. From now on, a new feature takes the next free number.
2. IDs are **never renumbered or reused**. If a `FE` or `BE` feature later gains its other half, keep the ID and change Scope to `FS`; the notes record when the second half arrived.
3. The planning card (Trello number, which is also the `la-<number>` branch name) is the source ticket. Use both in commit messages and pull request titles: `F000050 la-140: tags on lessons`.
4. Types: **Feature** (user-visible behavior) and **Technical** (CI/CD, tooling, refactoring, infrastructure users do not see). Bug fixes are not numbered; they are listed per release in [Release history](../release-history.md) with the card number of the bug.
5. Planning ideas are not numbered until code that implements them reaches the main line. See [Roadmap and gaps](roadmap-and-gaps.md).

Conventions used below:

- **Card** is the Trello card number from the exported board (`la-N`). `n/a` means no card was found and the commit message is the only reference.
- **Delivered by** lists commits and pull requests. `FE#34` is `language-app-frontend` PR #34 and `BE#3` is `backend-learning-platform` PR #3. The first frontend pull requests were opened in the original `karinazz/LanguageApp` repository and are written `K#n`. The first backend pull requests (2024) were opened in `Ewa-Anna/backend-learning-platform` and are written `E#n`; their numbers overlap with later `BE#n` numbers. A bare commit hash means there was no pull request.
- **Delivered** is the merge date, or the commit date when there was no pull request. Where backend and frontend differ, both are shown.
- **Release** refers to [Release history](../release-history.md).

## Register

| ID | Scope | Feature | Type | Card | Delivered by | Delivered | Release | Notes and known issues | Spec |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| F000001 | FE | Frontend foundation: Vite, React, TypeScript, MUI, Redux store | Technical | 12 | `3b416df`, `19a240a`, `0f483d3`, `76ce10f` | 2024-03-22 | R01 | | [Architecture](../architecture.md) |
| F000002 | FE | Landing page (navigation, hero, features, testimonials) | Feature | 19 | `0798502`, `93b1638`, `5fc6a22`, `0aae987` | 2024-04-10 | R01 | The "Features" section was removed in FE#14 (card 60, 2025-04-10). | [Public experience](public-experience.md) |
| F000003 | BE | Docker setup for the backend | Technical | 62 | `d726c10` (E#6 "Feature #2") | 2024-05-10 | R01 | | [Getting started](../getting-started.md) |
| F000004 | BE | Code quality and CI: flake8, GitHub workflows, Dependabot, tests; later ruff, pre-commit, GitHub Actions refresh | Technical | n/a | `db29c78` (E#7), `f0cbaff` (E#11), `26fbdce` (E#12), `ff9a545` (BE#10) | 2024-05-10 | R01, R02, R08 | Dependabot upgrades ran from 2024-06 to 2024-09. | [Contributing](../contributing.md) |
| F000005 | FS | Registration, login and JWT session | Feature | 25, 29, 61, 62, 82 | BE: `5da1f33` (E#3 "Feature #1"), `4bf5faa` (BE#5, CustomUser replaces TokenUser). FE: `eca8f0f` (K#6), `efdd271` (FE#7, Firebase removed), `eaedad3` + `3b94531` (FE#32) | 2024-05-10 BE, 2024-07-11 FE | R01, R02, R04, R06 | Replaced the early Firebase sign-in (F000007). BE fixes `309fd1f` (#30) and `3859701` (CSRF) in 2024-08. | [Authentication](authentication.md) |
| F000006 | FS | User profile and settings page | Feature | 31, 95 | BE: profile endpoint in `5da1f33`, fix `48c1088` (#34). FE: `e2fe11f` (K#7), la-95 text color (FE#37) | 2024-05-10 BE, 2024-08-27 FE | R01, R02, R07 | FE#37 changed the settings text color from white to black. | [Account and progress](account-and-progress.md) |
| F000007 | FE | Registration and login screens (Firebase, Redux auth, Google sign-in) | Feature | 12, 29 | K#1, K#2, K#4 (`61e0a5c`, `ff28040`, `39b7a21`) | 2024-05-20 | R01, R02 | Superseded by F000005. Firebase removed in FE#7 (2025-02-18). | [Authentication](authentication.md) |
| F000008 | FS | Lessons and phrase pairs (flashcards) CRUD | Feature | 32, 33, 34, 35, 78, 79 | BE: `950522c` (E#10 "Feature #8"). FE: `b1f05dc` (K#8, vocabulary inputs), `e576f88` (FE#1, add/edit lesson form), `80a1367` (FE#5, delete), `6b4a6a2` (FE#20, duplicate values fix) | 2024-06-12 BE, 2024-09-12 FE | R02, R03, R05 | Duplicate phrase pairs after editing a lesson were fixed in FE#20. | [Lesson authoring](lesson-authoring.md) |
| F000009 | BE | Backend main page | Feature | n/a | `31fcabc` | 2024-07-06 | R02 | | [Architecture](../architecture.md) |
| F000010 | FS | Lesson progress (learned flag, progress percent and progress bar) | Feature | 92, 109 | BE: `6e2da96` (E#19 "Feature #16", `is_learned`), `2e9b0ca` (rounded percent). FE: `94831b6` (FE#40, progress bar), `2b7057c` (FE#41, refresh after phrase pair update) | 2024-07-06 BE, 2026-02-25 FE | R02, R07 | Card 109 fixed the progress bar updating only after a page reload. | [Learning modes](learning-modes.md) |
| F000011 | BE | Lesson ownership and user statistics endpoint (`stats` app) | Feature | 80 | `d2daad5` (E#46 "Feature #45") | 2024-09-05 | R03 | The statistics endpoint is not used by the current frontend dashboard. | [Dashboard and organization](dashboard-and-organization.md) |
| F000012 | FE | Routing, public layout and 404 page | Feature | n/a | `d352bf2`, `45ebded`, `4ac12d7` (K#3) | 2024-09-16 | R03 | | [Public experience](public-experience.md) |
| F000013 | FE | User dashboard shell: sidebar, footer, main area | Feature | 28 | `9e26099`, `0835bd2`, `d9ac3d0` (K#5) | 2024-10-08 | R03 | | [Dashboard and organization](dashboard-and-organization.md) |
| F000014 | FE | Styling refactor: styled-components, theme colors and sizes, breakpoints | Technical | 52, 53, 54, 55, 56 | FE#4, FE#3, FE#6, FE#9, FE#10, FE#8 | 2024-12-18 to 2025-03-26 | R03, R04 | | [Architecture](../architecture.md) |
| F000015 | BE | MySQL and production hosting: prod Docker Compose, domain, allowed hosts, frontend URL whitelist | Technical | 50 | `24c1b08` to `fd144d3` (2025-01-14 to 2025-04-21), `463967f` (BE#5) | 2025-01-14 | R04, R06 | Configuration verified on 2026-11-26; see the Hosting and deployment section of the architecture page. | [Architecture](../architecture.md) |
| F000016 | FE | Frontend CI/CD and separate Netlify deploys for `main` and `develop` | Technical | 49 | `19d6de4` (FE#10), `f77c4ff` (FE#11), `7bdcff8` (FE#15) | 2025-03-21 | R04 | `VITE_API` build fix in FE#33 (2026-01-14). | [Contributing](../contributing.md) |
| F000017 | FE | Code quality and README: Prettier, ESLint fixes, README | Technical | 58, 59, 60 | FE#12, FE#13, `330c982` (FE#14) | 2025-03-26 | R04 | | [Contributing](../contributing.md) |
| F000018 | FE | Structure reorganization; separate login and register pages; dashboard layout | Technical | 57 | `ecbba1c` (FE#16), FE#17 | 2025-05-01 | R04 | | [Architecture](../architecture.md) |
| F000019 | FE | Display the user's lessons on the dashboard | Feature | 80 | `ca555ec` (FE#21) | 2025-07-04 | R05 | Pairs with F000011 (lesson ownership). | [Dashboard and organization](dashboard-and-organization.md) |
| F000020 | FE | Auth pages layout, back button, friendly registration errors | Feature | 73 | `2b0c2dd`, `3bc6534`, `60c25a8` (FE#18) | 2025-07-07 | R05 | | [Authentication](authentication.md) |
| F000021 | FE | Privacy policy page | Feature | 71 | `985ee9e` (FE#19) | 2025-07-23 | R05 | | [Public experience](public-experience.md) |
| F000022 | FE | Navigation bar: logo, navigation panel, hamburger menu; "learn more" no longer opens 404 | Feature | 64, 65, 66 | `32c1433`, `aafba3c`, `fd60a44` (FE#22, FE#25) | 2025-07-29 | R05 | | [Public experience](public-experience.md) |
| F000023 | FS | Forgot password and password reset by email | Feature | 74, 75, 110 | BE: BE#2 (`b01ca0c` email sender settings), `ff9eae4` (reset URL). FE: `8d674b3` (FE#23) | 2025-08-11 BE, 2025-08-27 FE | R05 | Open bug, card 110: reset password action can return status 400. | [Authentication](authentication.md) |
| F000024 | FE | Support page with FAQ | Feature | 70 | `83b210a`, `9e6c7af` (FE#24) | 2025-08-13 | R05 | | [Public experience](public-experience.md) |
| F000025 | FE | "Join now" from the contact form opens registration with the email prefilled; email validation; page title | Feature | 63, 72 | `d6ee9ae`, `9860d7d`, `3f88e3d` (FE#26) | 2025-08-27 | R05 | | [Public experience](public-experience.md) |
| F000026 | FE | About Us page | Feature | 67 | `180941c` (FE#29) | 2025-09-09 | R05 | | [Public experience](public-experience.md) |
| F000027 | FE | Flashcards learning page (first learning mode) and lesson card icons | Feature | 76 | `125b485`, `3b44072` (FE#28) | 2025-09-12 | R05 | | [Learning modes](learning-modes.md) |
| F000028 | FS | Sections with a default "Other" section; assign lessons to sections | Feature | 83, 84, 85, 86, 87 | BE: `cbd3f56` (BE#3). FE: `af903a0` (FE#34, sections), `72b58e1` + `f62f38a` (FE#35, section view, unassigned lessons) | 2025-10-19 BE, 2025-12-02 FE | R06 | Open ideas: unique names within a section (card 114), section color from backend (card 118). | [Dashboard and organization](dashboard-and-organization.md) |
| F000029 | FE | Browse and review modes for flashcards; lesson card component | Feature | 88 | `c18b7ae`, `5d019c6` (FE#31) | 2025-10-20 | R06 | | [Learning modes](learning-modes.md) |
| F000030 | FE | Contact Us page | Feature | 68 | `5209008` (FE#30) | 2025-10-27 | R06 | | [Public experience](public-experience.md) |
| F000031 | FS | Reset progress of a lesson or a section | Feature | 90, 91 | BE: `0ad6325` (BE#4; also removed `BasicAuthentication` and added section `color`). FE: `c2e4763` (FE#39) | 2025-11-04 BE, 2026-02-23 FE | R06, R07 | | [Learning modes](learning-modes.md) |
| F000032 | FE | Flashcard review animations (green and red border) | Feature | 93 | `d2ee46a` (FE#38) | 2026-01-27 | R07 | | [Learning modes](learning-modes.md) |
| F000033 | FE | Layout update: container with maximum width | Feature | 69 | `aecb09d` (FE#36) | 2026-02-16 | R07 | | [Public experience](public-experience.md) |
| F000034 | FE | Quiz lesson type (choose an answer) | Feature | 105 | `235201f` (FE#44) | 2026-03-24 | R07 | | [Learning modes](learning-modes.md) |
| F000035 | FS | Profile photo upload | Feature | 96, 97 | BE: `34b227e` (BE#7, upload with throttling and size limit). FE: `5f22c2b` + `76679bf` (FE#54, upload and URL preview) | 2026-03-24 BE, 2026-09-24 FE | R07, R10 | | [Account and progress](account-and-progress.md) |
| F000036 | BE | Deployment pipeline: SSH check, deploy action, migrate after deploy, secure proxy | Technical | n/a | `39e2518` (BE#11), `3128f05` (BE#12), `6639f16` (BE#13), `9c2020a` (BE#14), `7d06a4e` (BE#15) | 2026-05-05 | R08, R09 | Configuration verified on 2026-11-26; see the Hosting and deployment section of the architecture page. | [Architecture](../architecture.md) |
| F000037 | FE | Swipe flashcards on a phone (custom `useSwipe` hook) | Feature | 94 | `b32b397`, `3fd6fa6` (FE#46) | 2026-05-05 | R08 | | [Learning modes](learning-modes.md) |
| F000038 | FE | Lesson summary view (including quiz summary) | Feature | 89 | `42d0896`, `2364461` (FE#42) | 2026-05-06 | R08 | | [Learning modes](learning-modes.md) |
| F000039 | FE | UI texts moved to translation files (i18next) | Technical | 100 | `ddb979c` (FE#45) | 2026-05-06 | R08 | Written-answer texts moved in FE#47. | [Architecture](../architecture.md) |
| F000040 | FS | Daily study streak (days in a row) | Feature | 101, 102 | BE: `9ddf8ca` (BE#9, `streak`, `last_active`, `GET /user/streak/`, `POST /user/streak/update/`). FE: `2c54b4b` + `1d915e9` (FE#43, dashboard streak driven by the backend API) | 2026-05-14 BE, 2026-05-30 FE | R08 | QA findings on the backend (not fixed at the time of writing): the streak read returns a stale value after a gap, and the update uses `date.today()` instead of `timezone.localdate()`. The QA evidence is a local report that is not published. Duplicate update POSTs under React StrictMode are expected in development. | [Account and progress](account-and-progress.md) |
| F000041 | FE | Matching pairs lesson type | Feature | 107 | `4ce7d7e` (FE#48) | 2026-05-19 | R08 | | [Learning modes](learning-modes.md) |
| F000042 | FS | Account deactivation with confirmation and forced logout | Feature | 119, 120 | BE: `c23f5c5` (BE#16, refresh token blacklisted for inactive users). FE: `da52a17` (FE#49, logout and redirect), `6ff2160` (FE#53, confirmation dialog) | 2026-06-14 BE, 2026-07-18 FE | R09 | Manual QA on 2026-10-25 (local manual QA record, not published) recorded that the redirect, cleared credentials, and second-tab behavior still needed verification. | [Account and progress](account-and-progress.md) |
| F000043 | FE | Written answer lesson type | Feature | 103 | `8b524e2` (FE#47) | 2026-06-17 | R09 | | [Learning modes](learning-modes.md) |
| F000044 | FS | Lesson creation date and sorting by creation date | Feature | 125, 128 | BE: `7910902` (`Lesson.created_at`). FE: `359babd` (FE#51, sort lessons, creation date on the lesson card) | 2026-07-06 BE, 2026-10-22 FE | R09, R10 | | [Dashboard and organization](dashboard-and-organization.md) |
| F000045 | FE | Search lessons by name | Feature | 126 | `af7b267` (FE#50) | 2026-07-18 | R09 | | [Dashboard and organization](dashboard-and-organization.md) |
| F000046 | BE | Spaced repetition: review fields and `GET /sections/{id}/review/` | Feature | 127, 133 | `f9d0d72` (BE#18), `e03f777` (BE#20, review returns the cards scheduled for review) | 2026-08-12 | R09, R10 | Backend is delivered. Section review UI is pending in FE #58. | [Learning modes](learning-modes.md) |
| F000047 | BE | Custom message when the email is already registered | Feature | 129 | `b8fe8ec` (BE#19) | 2026-08-12 | R09 | Card 129 is labeled BE/FE. No dedicated frontend commit exists, so confirm how the frontend shows this message. | [Authentication](authentication.md) |
| F000048 | FE | The default "Other" section cannot be deleted (trash icon removed) | Feature | 113 | `88e72fb` (FE#55) | 2026-09-04 | R10 | The "Other" card keeps its edit icon. | [Dashboard and organization](dashboard-and-organization.md) |
| F000049 | FE | Cancel button on create and edit forms | Feature | 116 | `adb4f32` (FE#56) | 2026-10-11 | R10 | Manual QA on 2026-10-25 found the Cancel button on the lesson edit form but not on the section create, section edit, change password, and update profile forms (local manual QA record, not published). | [Lesson authoring](lesson-authoring.md) |
| F000050 | BE | Lesson tags with case-insensitive normalization, ownership, and repeated `tag` query filtering | Feature | 122, 123, 124 | `2e283b8` (BE#21) | 2026-11-03 | R11 | Updating a lesson adds submitted tags; the API does not yet demonstrate tag removal. Frontend authoring and filtering are not merged. | [Lesson authoring](lesson-authoring.md) |
| F000051 | BE | Language lessons with source and target language metadata and validation | Feature | 134, 135, 136 | `4ac3e64`, `0550cf3` (BE#22) | 2026-11-26 | R11 | Source and target languages are required for language lessons and must differ. Frontend selection and audio are pending; FE #59 currently uses mock speech-language codes. | [Lesson authoring](lesson-authoring.md) |

## Planned or open items (not numbered yet)

Cards below are not delivered. They receive an ID when code reaches the main line. Pull request references are as of 2026-11-26; use the live lists for the [frontend](https://github.com/LanguageAppSpace/language-app-frontend/pulls) and [backend](https://github.com/LanguageAppSpace/backend-learning-platform/pulls) for current status.

| Card | Item | State on the board |
| --- | --- | --- |
| 44, 45 | Admin panel and statistics (FE, BE) | Backlog |
| 46, 47 | Friends and shared statistics (FE, BE) | Research |
| 98, 99 | Learning goals; levels and points | Research |
| 110 | Bug (BE): reset password action returns status 400 | To Do |
| 111, 112 | Bug (BE): status 500 when creating a lesson or adding vocabulary in the default section | Doing |
| 114 | Unique section and lesson names | To Do |
| 117 | Bug (BE/FE): too many refresh calls or logout on page refresh | FE #57 open; needs integration testing |
| 118 | Bug (FE): section card does not use the color sent by the backend | To Do |
| 121 | Back button on subpages | To Do |
| 124 | Frontend tag authoring and filtering | Backend F000050 delivered; frontend remains open |
| 130 | Bug (BE/FE): "LanguageApp" looks clickable but does nothing | To Do |
| 132 | Bug (FE): registration form keeps old credentials after CREATE ACCOUNT | To Do |
| 133 | Banner with lessons to review | FE #58 open; backend F000046 delivered |
| 134, 135, 136 | Language lesson frontend selection and filtering | Backend F000051 delivered; frontend remains open |
| 137 | Flashcard audio | FE #59 open in draft and uses mock language codes |
| 139 | Wrap long section/lesson text | FE #60 open |

Board state is taken from a local Trello board export (last board activity 2026-09-02) and may be older than the live board. The raw export is not published because it contains team members' personal data; ask a project member to confirm the current state.

# Product Map

This page translates the planning material into a documentation map. Planning information was taken from a private Trello board export (last board activity 2026-09-02). The raw export is not published because it contains team members' personal data. The Trello and Miro boards are private, so their current state must be confirmed by a project member when it changes. Miro designs were not directly verified.

## Product areas

| Product area | Product intent from planning | Current implementation status | Specification |
| --- | --- | --- | --- |
| Public experience | Explain the product and provide entry points | Implemented routes and browser coverage | [Public experience](features/public-experience.md) |
| Authentication | Register, sign in, persist a session, sign out, recover a password | Implemented; backend and browser coverage exists | [Authentication](features/authentication.md) |
| Dashboard and organization | Show activity, sections, lessons, and empty states | Implemented; dashboard journey coverage exists | [Dashboard and organization](features/dashboard-and-organization.md) |
| Lesson authoring | Create, edit, delete lessons and phrase pairs | Implemented in frontend/backend; journey and backend coverage exists | [Lesson authoring](features/lesson-authoring.md) |
| Learning modes | Browse, review, quiz, matching pairs, written answer, section review, audio | Modes are implemented; section review and text-to-speech are pending in frontend PRs [#58](https://github.com/LanguageAppSpace/language-app-frontend/pull/58) and [#59](https://github.com/LanguageAppSpace/language-app-frontend/pull/59) (as of 2026-11-26) | [Learning modes](features/learning-modes.md) |
| Account and progress | Profile, password, deactivation, streak, progress reset | Implemented with partial browser coverage; session restoration is pending in frontend PR [#57](https://github.com/LanguageAppSpace/language-app-frontend/pull/57) (as of 2026-11-26) | [Account and progress](features/account-and-progress.md) |
| Lesson metadata | Tags, creation date, source language, target language, search, sorting | Backend tags and language fields are merged; frontend search/sorting are merged; frontend tag/language forms and filtering remain pending | [Lesson authoring](features/lesson-authoring.md) |
| Admin statistics | Admin panel and statistics | Backend statistics endpoint exists; a product admin UI is not confirmed | [Roadmap and gaps](features/roadmap-and-gaps.md) |

> Source baseline, 2026-11-26: frontend `develop` at `21a533e` and backend `main` at `fd93263`. Open pull requests change often; use the live lists for the [frontend](https://github.com/LanguageAppSpace/language-app-frontend/pulls) and [backend](https://github.com/LanguageAppSpace/backend-learning-platform/pulls).

## Planning status rules

- **Implemented** means code and a reachable route or endpoint exist in the main line.
- **Pending** means the work is in an open, unmerged pull request. Do not describe it as shipped behavior.
- **Partially covered** means implementation exists but one or more acceptance criteria lack an automated test or are not fully consistent across frontend and backend.
- **Planned** means the idea appears in Trello/Miro or the export but is not represented by a current implementation path.

## Roadmap themes from Trello

The export contains cards for language selection, notifications, quests, admin statistics, goals, friends, lesson sorting/search, tags, review reminders, language filters, audio, and account deactivation confirmation. Search, sorting, backend tags, and backend language metadata are delivered. Section review, text-to-speech, session restoration, and long-text wrapping were pending in open frontend pull requests ([#57](https://github.com/LanguageAppSpace/language-app-frontend/pull/57), [#58](https://github.com/LanguageAppSpace/language-app-frontend/pull/58), [#59](https://github.com/LanguageAppSpace/language-app-frontend/pull/59), [#60](https://github.com/LanguageAppSpace/language-app-frontend/pull/60)) as of 2026-11-26. The [Roadmap and gaps](features/roadmap-and-gaps.md) page details these items.

## Feature documentation format

Every feature page follows the same traceability chain:

```text
Planning source -> user story -> acceptance criteria -> UI/API implementation -> automated tests -> manual gap checks
```

When a card or Miro flow is refined, update the affected feature page and add or update a test in the relevant repository in the same change.

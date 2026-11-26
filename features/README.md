# Feature Specifications

These pages describe the product as behavior, not only as code. Each page starts with a user story and connects expected behavior to implementation and tests.

## Implemented journeys

- [Public experience](public-experience.md)
- [Authentication](authentication.md)
- [Dashboard and organization](dashboard-and-organization.md)
- [Lesson authoring](lesson-authoring.md)
- [Learning modes](learning-modes.md)
- [Account and progress](account-and-progress.md)

## Traceability

- [Feature register](feature-register.md): every delivered feature with its ID (`Fxxxxxx`), scope (FE, BE, FS), card, pull requests, release, and specification page.
- [Release history](../release-history.md): releases `R01` to `R11` and what each contained.

## Roadmap and gaps

- [Roadmap and gaps](roadmap-and-gaps.md): Trello/Miro ideas that need clarification, implementation, or test coverage.

## Feature page contract

Every feature page should answer:

1. Who is the user and what outcome do they need?
2. What must happen on the happy path?
3. What must happen for invalid input, missing data, unauthorized access, and service failure?
4. Which frontend routes/components and backend endpoints/models implement it?
5. Which automated tests verify it?
6. What is still a manual check, test gap, or planned extension?
7. Which feature IDs from the [Feature register](feature-register.md) does this page cover?

## Conventions

- Paths such as `language-app-frontend/src/...` and `backend-learning-platform/backend/...` are relative to the [frontend](https://github.com/LanguageAppSpace/language-app-frontend) and [backend](https://github.com/LanguageAppSpace/backend-learning-platform) repositories.
- Test file paths (`test/...`) belong to the pre-migration test workspace. They are not available in [language-app-tests](https://github.com/LanguageAppSpace/language-app-tests) yet, and not all of them are committed anywhere. They record existing coverage; they are not runnable commands.
- Pull request status is dated. For current status use the live lists for the [frontend](https://github.com/LanguageAppSpace/language-app-frontend/pulls) and [backend](https://github.com/LanguageAppSpace/backend-learning-platform/pulls).

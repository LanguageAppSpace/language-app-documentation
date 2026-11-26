# LanguageApp documentation

Learners can organize phrase pairs into lessons and sections, then practice with
flashcards and quizzes. Start with [local setup](getting-started.md) to try the
app or [contributing](contributing.md) to document a change.

## Repositories

- [Frontend](https://github.com/LanguageAppSpace/language-app-frontend): React web app.
- [Backend](https://github.com/LanguageAppSpace/backend-learning-platform): Django API for accounts, lessons and progress.
- [Tests](https://github.com/LanguageAppSpace/language-app-tests): planned home for shared browser tests. Migration is not complete; do not assume suites run from this repository yet.
- [Documentation](https://github.com/LanguageAppSpace/language-app-documentation): product behavior and guidance that spans repositories.

## Documentation map

- [Getting started](getting-started.md): run the frontend and backend locally.
- [Product map](product-map.md): product areas and their implementation status.
- [Architecture](architecture.md): components, hosting and deployment, and backend versus frontend delivery status.
- [Feature specifications](features/README.md): user stories, expected behavior and implementation notes for each product area.
- [Feature register](features/feature-register.md): numbered features with scope, cards, pull requests and releases.
- [Release history](release-history.md): reconstructed milestones R01 to R11.
- [API documentation](api.md): backend API entry points and lesson and section contracts.
- [Testing](testing.md): where tests live today, the shared-staging warning and the pre-migration harness.
- [Isolated local staging](local-staging.md): the pre-migration local stack for browser tests.
- [Repository status](repository-status.md): dated snapshot of source revisions and delivered changes.
- [Contributing](contributing.md): how to change the documentation and keep the register consistent.

## Publication plan

The documentation is published as a stack of pull requests, merged in order:

1. **PR 1: Foundation.** This README, getting started and contributing guidance.
2. **PR 2: Product, architecture and features.** Product map and architecture (PR 2A); feature register, specifications, release history, templates and the consistency checker (PR 2B).
3. **PR 3: Developer guides.** Testing, local staging and API documentation. Test paths and commands are verified against the test migration before they are published as instructions.
4. **PR 4: Maintenance.** Review of the roadmap and repository status pages. Automated documentation checks, CI, ownership and versioning guidance are not scheduled yet.

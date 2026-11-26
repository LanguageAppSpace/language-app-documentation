# LanguageApp documentation

Learners can organize phrase pairs into lessons and sections, then practice with
flashcards and quizzes. Start with [local setup](getting-started.md) to try the
app or [contributing](contributing.md) to document a change.

## Repositories

- [Frontend](https://github.com/LanguageAppSpace/language-app-frontend): React web app.
- [Backend](https://github.com/LanguageAppSpace/backend-learning-platform): Django API for accounts, lessons and progress.
- [Tests](https://github.com/LanguageAppSpace/language-app-tests): planned home for shared browser tests. Migration is not complete; do not assume suites run from this repository yet.
- [Documentation](https://github.com/LanguageAppSpace/language-app-documentation): product behavior and guidance that spans repositories.

## Publication plan

After this foundation merges, publish each group in a separate PR, in order:

1. **PR 2: Product and architecture.** Product map, architecture, feature register, specifications and release history.
2. **PR 3: Developer guides.** Setup, environments, API, test instructions, coverage and known gaps. Verify test paths against the migration before publishing commands.
3. **PR 4: Maintenance.** Automated documentation and link checks, CI, ownership and versioning.

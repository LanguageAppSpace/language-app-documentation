# Repository Status

Audit date: 2026-11-26

This page records the public GitHub state used for the latest documentation review. It is a point-in-time snapshot that is not updated automatically. Check the repositories and the live pull request lists before relying on it for a merge or release decision. Local checkout state is deliberately not recorded here.

## Source revisions

| Repository | Main line | Revision | Latest commit |
| --- | --- | --- | --- |
| [Frontend](https://github.com/LanguageAppSpace/language-app-frontend) | `develop` | `21a533e` | 2026-10-22 |
| [Backend](https://github.com/LanguageAppSpace/backend-learning-platform) | `main` | `fd93263` | 2026-11-26 |

## Merged since the previous documentation baseline

- Backend [#21](https://github.com/LanguageAppSpace/backend-learning-platform/pull/21), 2026-11-03: lesson tags, user-scoped tag records, tag filtering (migration `0007`).
- Backend [#22](https://github.com/LanguageAppSpace/backend-learning-platform/pull/22), 2026-11-26: language-lesson flag, source language, target language, and validation (migration `0008`).

These changes are documented as delivered backend features F000050 and F000051 in the [Feature register](features/feature-register.md).

## Open pull requests

Pull request status changes often and is not copied into this page. Use the live lists:

- [Frontend pull requests](https://github.com/LanguageAppSpace/language-app-frontend/pulls)
- [Backend pull requests](https://github.com/LanguageAppSpace/backend-learning-platform/pulls)

The specific pending frontend pull requests that documentation depends on are listed, with their date, under [Pull request dependencies](features/roadmap-and-gaps.md#pull-request-dependencies). Do not describe their content as shipped behavior until they are merged.

## Documentation conclusions

As of 2026-11-26:

- Search, creation-date sorting, backend tags, and backend language fields are delivered capabilities.
- Frontend tag authoring and filtering and language selection are not delivered.
- Spaced-repetition endpoints are delivered by the backend; the section review interface is not merged.
- Flashcard speech and session restoration are not merged.

## Refresh procedure

1. Check the latest commit on frontend `develop` and backend `main` on GitHub.
2. Check the live pull request lists above.
3. Update the [Feature register](features/feature-register.md), [Release history](release-history.md), affected feature pages, [Roadmap and gaps](features/roadmap-and-gaps.md), and this snapshot together.
4. Run `python tools/add_feature.py --check` before opening the pull request.

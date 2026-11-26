# Roadmap and Gaps

This page keeps ideas from planning visible without describing them as shipped behavior. Reviewed on 2026-11-26.

Planning evidence comes from a private Trello export that may be older than the live board. Pull request status is not copied into the table below; the few pull requests that documentation depends on are listed, with their date, under [Pull request dependencies](#pull-request-dependencies).

## Planned or requiring clarification

| Theme | Planning evidence | Current documentation status | Next definition needed |
| --- | --- | --- | --- |
| Language selection and language-specific lessons | Trello cards 134-137 | Backend language fields and validation are merged (BE #22). Frontend selection is not in `develop`; flashcard audio is a draft frontend pull request that uses mock language codes. | Consume `is_language_lesson`, `source_language`, and `target_language`; add language selectors and replace the mock speech languages. |
| Review reminders and spaced repetition | Trello cards 127 and 133 | Backend due-card endpoint is merged. The section review banner and route are in an open frontend pull request. | Verify that correct/incorrect review answers persist and reschedule cards before merge. |
| Lesson tags | Trello cards 122-124 | Backend tag create/update and `?tag=` filtering are merged in BE #21. Frontend authoring/filtering is not confirmed. | Define tag input, chip display, removal semantics, and combined filters. |
| Lesson search and sorting | Trello cards 125-126 and 128 | Frontend search and creation-date sorting are delivered; lesson `created_at` is delivered by the backend. | Add end-to-end tests for combined search/sort states and large lists. |
| Session restoration on refresh | Trello card 117 | Implemented in an open frontend PR, not merged to `develop`. | Test refresh, expired token, multiple simultaneous 401s, and public auth endpoints. |
| Long lesson and section text | Card 139 | Open frontend PR adds `overflowWrap: anywhere` to section and lesson titles/descriptions. | Verify at mobile and desktop widths with long unbroken strings. |
| Goals, quests, points, levels | Trello ideas | Planned | Define measurement, rewards, persistence, and anti-abuse rules. |
| Friends and shared statistics | Trello cards for adding friends and viewing statistics | Planned | Define privacy, permissions, invitations, and visible metrics. |
| Admin statistics | Frontend/backend admin statistics cards | Not confirmed in current app surface | Define roles, metrics, time ranges, and authorization. |
| Notifications | Trello card | Current app has local success/error notifications | Define persistent notification types and delivery rules. |
| Account deactivation | Trello idea and current endpoint | Frontend confirmation and forced logout are delivered; a complete browser journey still needs strengthening. | Define retention and recovery behavior. |

## Pull request dependencies

Pull request status changes often and is not copied into this page. Use the live lists for the [frontend](https://github.com/LanguageAppSpace/language-app-frontend/pulls) and [backend](https://github.com/LanguageAppSpace/backend-learning-platform/pulls).

These frontend pull requests were open on 2026-11-26 and are referenced by the specification pages or the table above. Check the live lists before relying on them, and do not describe their content as shipped behavior until they are merged:

- [#57](https://github.com/LanguageAppSpace/language-app-frontend/pull/57) restores access tokens before protected requests (Authentication).
- [#58](https://github.com/LanguageAppSpace/language-app-frontend/pull/58) adds section review banners and a section-wide review route (Learning modes).
- [#59](https://github.com/LanguageAppSpace/language-app-frontend/pull/59) is a draft that adds flashcard text-to-speech with mock language codes (Learning modes).
- [#60](https://github.com/LanguageAppSpace/language-app-frontend/pull/60) wraps long section and lesson titles and descriptions (Lesson authoring).
- [#61](https://github.com/LanguageAppSpace/language-app-frontend/pull/61) is titled "LA-116: cancel button on the forms (fix)" and changes `SectionModal.tsx`. Whether it resolves the Cancel-button QA finding recorded for F000049 has not been verified (Lesson authoring).

## Definition of ready

A roadmap feature is ready for implementation when its page contains:

- a user story
- acceptance criteria for success, validation, authorization, empty state, and failure
- a Miro or other design reference
- an API/data contract if needed
- a test matrix with at least one automated acceptance scenario
- an explicit decision about analytics, accessibility, and mobile behavior

## Current test gaps

The most important gaps discovered from the code and test inventory are:

- full browser journeys for browse, review, quiz, matching pairs, and written answer
- lesson edit persistence (section edit and delete, and lesson delete and reset, are covered; see [Dashboard and organization](dashboard-and-organization.md#tests))
- a password-change browser journey (profile and deactivation are covered; see [Account and progress](account-and-progress.md#tests))
- cross-user authorization for sections, lessons, and phrase pairs opened by URL or API (only the dashboard section list is checked)
- direct 404 and public-page responsive coverage

These gaps should become test tasks rather than informal manual knowledge. Coverage statements refer to the tests described in [Testing](../testing.md), most of which have not been migrated to language-app-tests yet.

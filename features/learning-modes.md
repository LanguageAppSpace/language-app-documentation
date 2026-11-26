# Learning Modes

**Feature IDs:** F000010, F000027, F000029, F000031, F000032, F000034, F000037, F000038, F000041, F000043, F000046. See the [Feature register](feature-register.md).

## User story

As a learner, I want to choose a practice mode for a lesson and receive immediate feedback and a useful summary, so that I can learn new phrase pairs and focus on the ones I have not mastered.

## Available modes

| Mode | Route | Expected behavior |
| --- | --- | --- |
| Browse | `/flashcards/:lessonId/browse` | View phrase pairs, flip between the two sides, and navigate forward/backward. |
| Review | `/flashcards/:lessonId/review` | Mark answers correct or incorrect, show review feedback, summarize results, and offer another pass over incorrect phrases. |
| Quiz | `/flashcards/:lessonId/quiz` | Select one answer from options, lock the response, show correct/incorrect state, advance, and show a summary/restart action. |
| Matching pairs | `/flashcards/:lessonId/matching` | Match related phrase pairs, prevent invalid completed selections, and finish with a result. |
| Written answer | `/flashcards/:lessonId/written-answer` | Enter an answer, compare it with the expected phrase, show feedback, and continue through the session. |

## Expected behavior for every mode

- Loading, missing lesson, empty lesson, and API error states are visible and actionable.
- Only phrases belonging to the selected lesson are shown.
- Progress through the session is visible where the mode supports it.
- A correct or learned answer updates phrase-pair state through the API when required.
- The learner can finish or restart without losing unrelated lesson data.
- Keyboard and mobile interactions remain usable, especially for answer controls.
- A backend language lesson carries source and target language values that can drive pronunciation later.

## Section review

The backend supports `GET /flashcards/sections/:id/review/`. It returns learned phrase pairs whose `next_review` time has arrived and exposes the due count as `review_count` on serialized sections.

As of 2026-11-26, [FE #58](https://github.com/LanguageAppSpace/language-app-frontend/pull/58) is open with a proposed `/section/:sectionId/review/cards` route and a review banner on section cards. It is not merged behavior. The proposed correct/incorrect controls currently advance through the set in the same way, so persistence and rescheduling of an answer need verification before this flow is accepted.

## Text-to-speech

As of 2026-11-26, [FE #59](https://github.com/LanguageAppSpace/language-app-frontend/pull/59) is an open draft that adds speech controls to both sides of a flashcard. It currently supplies hard-coded `pl-PL` and `en-US` values. It must be integrated with the backend `source_language` and `target_language` fields before the feature is considered complete. Those fields and their validation are specified in [Lesson authoring](lesson-authoring.md), which owns the language-lesson feature.

## Implementation trace

- Routes: `language-app-frontend/src/config/route.config.ts`.
- Shared state and review logic: `src/Lessons/Flashcards/context/FlashcardsProvider.tsx` and `src/Lessons/Flashcards/context/FlashcardsContext.tsx`.
- Browse/review data loading: `src/Lessons/Flashcards/hooks/useFlashcards.tsx`.
- Quiz: `src/Lessons/Quiz/`.
- Matching pairs: `src/Lessons/MatchingPairs/`.
- Written answer: `src/Lessons/WrittenAnswer/`.
- Phrase state API: `src/redux/lessons/lessonsApiSlice.ts`, endpoint `PATCH flashcards/:lessonId/pairs/:pairId/`.

## Tests

> **Note:** Test file paths below belong to the pre-migration test workspace. They are not available in [language-app-tests](https://github.com/LanguageAppSpace/language-app-tests) yet, and not all of them are committed anywhere. They record existing coverage; they are not runnable commands.
>
> Test instructions: pending migration to language-app-tests

The backend suite verifies phrase-pair updates, deletion, calculated progress, review scheduling, and due-card filtering. The dashboard journey verifies opening the lesson mode dialog. Dedicated browser coverage for each full learning mode and the proposed section-review/audio flows is currently a gap and should be added as focused journeys.

Recommended scenarios:

- browse: flip, next, previous, first/last boundary
- review: correct, incorrect, finish, retry incorrect phrases, persistence
- quiz: select answer, lock answer, next, summary, restart
- matching: valid match, invalid match, completion, restart
- written answer: exact answer, incorrect answer, empty answer, completion

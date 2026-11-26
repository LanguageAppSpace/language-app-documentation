# API Documentation

The backend exposes interactive API documentation through Swagger when the development environment is running.

- Swagger UI: [http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/)

Start the backend using the instructions in [Getting Started](getting-started.md) before opening the link.

The backend API currently supports authentication, profiles, streaks, flashcard-based learning, progress tracking, tags, language lesson metadata, and spaced repetition. Treat the generated Swagger schema and backend serializers/views as the source of truth when documenting request and response details. The contracts below were checked against backend `main` at `fd93263` on 2026-11-26.

## Lesson and section contracts

### Lessons

Lesson payloads can include:

- `tags`: a list of tag names; backend names are trimmed and case-normalized
- `is_language_lesson`: whether the lesson uses source/target language metadata
- `source_language`: required when `is_language_lesson` is true
- `target_language`: required when `is_language_lesson` is true and must differ from the source language
- `created_at`: backend-generated timestamp (read-only)

List filtering supports repeated tag parameters, for example:

```text
GET /flashcards/lessons/?tag=travel&tag=polish
```

Each tag condition is applied as a filter. The backend currently adds submitted tags during update; explicit removal behavior must be defined.

### Sections and reviews

- `GET /flashcards/sections/` includes `review_count` in serialized sections.
- `GET /flashcards/sections/{id}/review/` returns learned cards whose scheduled review time is due.
- `POST /flashcards/lessons/{id}/reset-progress/` resets lesson phrase progress.
- `POST /flashcards/sections/{id}/reset-progress/` resets section phrase progress.

As of 2026-11-26, [FE #58](https://github.com/LanguageAppSpace/language-app-frontend/pull/58) proposes the frontend consumer for section review. It is open and not part of merged frontend behavior.

## API change checklist

When an API contract changes, update the backend implementation, migrations, generated schema, affected frontend types/API calls, tests, and this documentation in the same pull request.

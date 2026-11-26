# Contributing

Open a documentation PR for one change a reader needs to understand. When an
application change spans repositories, link the relevant implementation PR or
source revision and identify whether the change affects the frontend or backend.

- **Implemented** means the behavior is present in merged code. A merge alone does not prove deployment or passing tests.
- **Planned** means the behavior is proposed or in an unmerged PR. For partial delivery, say which part exists and which is still planned.
- Before requesting review, preview the Markdown, open its links and check setup instructions against the named revision. State what you verified and what you did not run.
- When you change the register, release history, or a feature specification, run `python tools/add_feature.py --check` and fix every reported problem.
- Link across repositories using GitHub URLs, not local checkout paths. Keep private board exports, workspace state, credentials, environment files and raw test evidence out of PRs.

## Releases and feature IDs

Use the form and script instead of editing the register by hand:

1. Copy [feature-form.txt](templates/feature-form.txt) and fill in the fields (scope, title, cards, delivered by, date, release, spec page).
2. Preview: `python tools/add_feature.py my-feature.txt --dry-run`
3. Apply: `python tools/add_feature.py my-feature.txt`

The script takes the next free ID (`Fxxxxxx`), adds the row to the [Feature register](features/feature-register.md), adds a line to the release in [Release history](release-history.md) (it creates the release when `release_period` and `release_theme` are filled in), adds the ID to the spec page's "Feature IDs" line, creates the spec page from [feature-page.md](templates/feature-page.md) when it does not exist, and then runs the consistency check. Fill in the `TODO` sections of a new spec page by hand.

Run `python tools/add_feature.py --check` at any time, and before opening a pull request. It fails on duplicate or skipped IDs, IDs missing from the register or from a release, missing scope, release or spec page, old-style IDs, and broken links.

Rules:

- Scope is `FE` (frontend only), `BE` (backend only) or `FS` (both delivered together). Never renumber or reuse an ID. When the other half of a `FE` or `BE` feature arrives, keep the ID, change Scope to `FS`, and add the date and PR to Notes by hand.
- Put the ID and the card in the pull request title, for example `F000050 la-140: tags on lessons`.
- Bug fixes are not numbered. List them under **Fixes** in the release by card number.
- Tag each release in both application repositories (for example `v1.1.0`) so the history no longer has to be reconstructed.

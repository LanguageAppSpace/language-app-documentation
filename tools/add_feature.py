"""Add a feature to the documentation from a filled form, or check the documentation for consistency.

Usage:
    python tools/add_feature.py FORM.txt [--dry-run]
    python tools/add_feature.py --check

Use --docs PATH to work on another copy of the documentation folder.
Only the Python standard library is used.
"""

import argparse
import re
import sys
from pathlib import Path
from urllib.parse import unquote

DOCS = Path(__file__).resolve().parent.parent
SCOPES = ("FE", "BE", "FS")
REQUIRED = ("scope", "title", "cards", "delivered_by", "delivered", "release", "spec")
ID_RE = re.compile(r"\bF\d{6}\b")
ROW_RE = re.compile(r"^\| (F\d{6}) \|")
LEGACY_RE = re.compile(r"\b(?:FE|BE|FS)\d{6}\b")


class Doc:
    """A Markdown file edited in memory; the original line endings are kept."""

    def __init__(self, path):
        self.path = Path(path)
        raw = self.path.read_bytes().decode("utf-8-sig")
        self.eol = "\r\n" if "\r\n" in raw else "\n"
        self.lines = raw.replace("\r\n", "\n").split("\n")

    def save(self):
        self.path.write_bytes(self.eol.join(self.lines).encode("utf-8"))

    def find(self, predicate, start=0):
        for i in range(start, len(self.lines)):
            if predicate(self.lines[i]):
                return i
        return -1


def read_text(path):
    return Path(path).read_text(encoding="utf-8-sig")


def read_form(path):
    values = {}
    for number, line in enumerate(read_text(path).splitlines(), 1):
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if ":" not in line:
            raise ValueError(f"Form line {number} is not 'key: value': {line!r}")
        key, value = line.split(":", 1)
        values[key.strip()] = value.strip()
    return values


def validate_form(form):
    problems = []
    for key in REQUIRED:
        if not form.get(key):
            problems.append(f"Field '{key}' is required.")
    scope = form.get("scope", "")
    if scope and scope not in SCOPES:
        problems.append(f"Field 'scope' must be one of {', '.join(SCOPES)}; got {scope!r}.")
    if form.get("delivered") and not re.match(r"^\d{4}-\d{2}-\d{2}", form["delivered"]):
        problems.append("Field 'delivered' must start with a date in the form YYYY-MM-DD.")
    if form.get("release") and not re.fullmatch(r"R\d{2}", form["release"]):
        problems.append("Field 'release' must look like R11.")
    if form.get("spec") and not re.fullmatch(r"[a-z0-9-]+", form["spec"]):
        problems.append("Field 'spec' must be a file name without .md: lowercase letters, digits and dashes.")
    if form.get("type") and form["type"] not in ("Feature", "Technical"):
        problems.append("Field 'type' must be Feature or Technical.")
    for key, value in form.items():
        if "|" in value:
            problems.append(f"Field '{key}' must not contain the | character (it breaks the table).")
    return problems


def register_rows(register):
    return [(m.group(1), line) for line in register.lines if (m := ROW_RE.match(line))]


def next_id(register):
    numbers = [int(row_id[1:]) for row_id, _ in register_rows(register)]
    return f"F{(max(numbers) if numbers else 0) + 1:06d}"


def page_title(path):
    for line in read_text(path).splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return Path(path).stem


def add_feature_id_to_spec(page_path, feature_id):
    page = Doc(page_path)
    index = page.find(lambda line: line.startswith("**Feature IDs:**"))
    if index == -1:
        raise ValueError(f"{page_path.name} has no '**Feature IDs:**' line.")
    page.lines[index] = re.sub(
        r"(\*\*Feature IDs:\*\* .*?)\. See", rf"\1, {feature_id}. See", page.lines[index], count=1
    )
    page.save()


def release_heading_index(history, release):
    return history.find(lambda line: line.startswith(f"## {release}:"))


def add_release_line(history, form, feature_id):
    start = release_heading_index(history, form["release"])
    end = history.find(lambda line: line.startswith("## "), start + 1)
    date = form["delivered"].split(",")[0].split(" ")[0]
    bullet = f"- {feature_id} ({form['scope']}) {form['title']} ({date})."
    features = history.find(lambda line: line.strip() == "**Features**", start)
    if features == -1 or features > end:
        history.lines[start + 1 : start + 1] = ["", "**Features**", "", bullet]
        return
    last = features
    for i in range(features + 1, end):
        if history.lines[i].startswith("- "):
            last = i
        elif history.lines[i].startswith("**"):
            break
    history.lines.insert(last + 1, bullet)


def add_overview_id(history, release, feature_id):
    index = history.find(lambda line: line.startswith(f"| [{release}]"))
    if index == -1:
        return
    cells = history.lines[index].rstrip().rstrip("|").rstrip()
    history.lines[index] = f"{cells}, {feature_id} |" if not cells.endswith("|") else f"{cells} {feature_id} |"


def add_release(history, form):
    release = form["release"]
    if not form.get("release_period") or not form.get("release_theme"):
        raise ValueError(
            f"Release {release} does not exist. Fill in 'release_period' and 'release_theme' to create it."
        )
    heading = f"{release}: {form['release_period']} {form['release_theme']}"
    anchor = re.sub(r"[^a-z0-9 -]", "", heading.lower()).replace(" ", "-")
    row = f"| [{release}](#{anchor}) | {form['release_period']} | {form['release_theme']} | |"
    table_end = max(i for i, line in enumerate(history.lines) if line.startswith("| [R"))
    history.lines.insert(table_end + 1, row)
    section = history.find(lambda line: line.startswith("## Test workspace history"))
    history.lines[section:section] = [f"## {heading}", "", "**Features**", "", ""]


def add_feature(docs, form, dry_run):
    problems = validate_form(form)
    if problems:
        raise ValueError("\n".join(problems))
    register = Doc(docs / "features" / "feature-register.md")
    history = Doc(docs / "release-history.md")
    feature_id = next_id(register)
    spec_path = docs / "features" / f"{form['spec']}.md"
    creates_page = not spec_path.exists()
    plan = []

    if release_heading_index(history, form["release"]) == -1:
        add_release(history, form)
        plan.append(f"Create release {form['release']} in release-history.md")

    spec_title = form.get("spec_title") or (form["title"] if creates_page else page_title(spec_path))
    if creates_page:
        page = (docs / "templates" / "feature-page.md").read_text(encoding="utf-8").format(
            spec_title=spec_title,
            feature_id=feature_id,
            user_story=form.get("user_story") or "TODO: write the user story.",
            happy_path=form.get("happy_path") or "TODO: describe the happy path.",
        )
        plan.append(f"Create spec page features/{form['spec']}.md from the template")
    else:
        plan.append(f"Add {feature_id} to the Feature IDs line of features/{form['spec']}.md")

    row = (
        f"| {feature_id} | {form['scope']} | {form['title']} | {form.get('type') or 'Feature'} | {form['cards']} | "
        f"{form['delivered_by']} | {form['delivered']} | {form['release']} | {form.get('notes', '')} | "
        f"[{spec_title}]({form['spec']}.md) |"
    )
    last_row = max(i for i, line in enumerate(register.lines) if ROW_RE.match(line))
    register.lines.insert(last_row + 1, row)
    plan.append(f"Add row {feature_id} to features/feature-register.md")
    add_release_line(history, form, feature_id)
    add_overview_id(history, form["release"], feature_id)
    plan.append(f"Add a line to {form['release']} in release-history.md")

    print(f"New feature ID: {feature_id}")
    for item in plan:
        print(f"  - {item}")
    if dry_run:
        print("Dry run: no files were changed.")
        return
    if creates_page:
        spec_path.write_bytes(page.encode("utf-8"))
    else:
        add_feature_id_to_spec(spec_path, feature_id)
    register.save()
    history.save()
    print("Files written. Review the diff.")


def check(docs):
    errors = []
    register = Doc(docs / "features" / "feature-register.md")
    history_text = read_text(docs / "release-history.md")
    rows = register_rows(register)
    ids = [row_id for row_id, _ in rows]
    if len(set(ids)) != len(ids):
        errors.append("Register has duplicate IDs.")
    if [int(i[1:]) for i in ids] != list(range(1, len(ids) + 1)):
        errors.append("Register IDs are not a continuous sequence F000001, F000002, ... in order.")
    releases = set(re.findall(r"^## (R\d{2}):", history_text, re.MULTILINE))
    spec_ids = {}
    for row_id, line in rows:
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) != 10:
            errors.append(f"{row_id}: row has {len(cells)} columns, expected 10.")
            continue
        _, scope, title, type_, card, delivered_by, delivered, release, _notes, spec = cells
        if scope not in SCOPES:
            errors.append(f"{row_id}: Scope {scope!r} is not one of {', '.join(SCOPES)}.")
        if type_ not in ("Feature", "Technical"):
            errors.append(f"{row_id}: Type {type_!r} is not Feature or Technical.")
        for field, value in (("Feature", title), ("Card", card), ("Delivered by", delivered_by), ("Delivered", delivered)):
            if not value:
                errors.append(f"{row_id}: {field} is empty.")
        for release_id in re.findall(r"R\d{2}", release):
            if release_id not in releases:
                errors.append(f"{row_id}: release {release_id} does not exist in release-history.md.")
        if not re.search(rf"^- {row_id} ", history_text, re.MULTILINE):
            errors.append(f"{row_id}: has no line in release-history.md.")
        match = re.search(r"\]\(([^)]+\.md)\)", spec)
        if not match:
            errors.append(f"{row_id}: Spec is not a link to a .md page.")
        elif not (docs / "features" / match.group(1)).exists():
            errors.append(f"{row_id}: spec page {match.group(1)} does not exist.")
        else:
            spec_ids.setdefault(match.group(1), set()).add(row_id)
    known = set(ids)
    for found in sorted(set(ID_RE.findall(history_text)) - known):
        errors.append(f"release-history.md mentions {found}, which is not in the register.")
    for page in sorted((docs / "features").glob("*.md")):
        match = re.search(r"^\*\*Feature IDs:\*\* (.*?)\. See", read_text(page), re.MULTILINE)
        if not match:
            continue
        listed = set(ID_RE.findall(match.group(1)))
        for unknown in sorted(listed - known):
            errors.append(f"{page.name}: lists {unknown}, which is not in the register.")
        for missing in sorted(spec_ids.get(page.name, set()) - listed):
            errors.append(f"{page.name}: the register links {missing} here but the Feature IDs line does not list it.")
    pages = [*docs.glob("*.md"), *(docs / "features").glob("*.md")]
    for path in pages:
        text = read_text(path)
        if LEGACY_RE.search(text):
            errors.append(f"{path.name}: old-style ID {LEGACY_RE.search(text).group(0)} found. Use Fxxxxxx.")
        for target in re.findall(r"\]\(([^)#:]+\.md)", text):
            if not (path.parent / unquote(target)).exists():
                errors.append(f"{path.name}: broken link to {target}.")
    if errors:
        print("Documentation check FAILED:")
        for error in dict.fromkeys(errors):
            print(f"  - {error}")
        return 1
    print(f"Documentation check passed: {len(ids)} features, {len(releases)} releases.")
    return 0


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("form", nargs="?", help="filled feature form (see templates/feature-form.txt)")
    parser.add_argument("--check", action="store_true", help="check the documentation for consistency")
    parser.add_argument("--dry-run", action="store_true", help="show what would change without writing files")
    parser.add_argument("--docs", default=str(DOCS), help="documentation folder (default: this repository's)")
    args = parser.parse_args()
    docs = Path(args.docs)
    if args.check:
        return check(docs)
    if not args.form:
        parser.error("give a form file, or use --check")
    try:
        add_feature(docs, read_form(args.form), args.dry_run)
    except ValueError as error:
        print(f"Error: {error}")
        return 1
    return 0 if args.dry_run else check(docs)


if __name__ == "__main__":
    sys.exit(main())

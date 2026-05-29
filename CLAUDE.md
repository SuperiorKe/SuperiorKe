# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

This is Kenn Macharia's GitHub profile repository. It contains:
- `github_profile.py` — an interactive CLI profile script
- `README.md` — the rendered GitHub profile page

## Running the profile script

```bash
python github_profile.py                          # greeting + usage hints
python github_profile.py --name "Visitor"         # personalized greeting
python github_profile.py --interest "AI agents"   # project recommendation
python github_profile.py --stats                  # live GitHub repo stats (requires requests)
python github_profile.py --report                 # formatted text report
python github_profile.py --save json              # save profile to JSON file
```

Install optional dependencies:
```bash
pip install termcolor requests
```

## Architecture of github_profile.py

Single-file, single-class design — `AIBuilder` holds all profile data and logic.

**Data** is declared in `__init__`:
- `self.projects` — list of project dicts, each with `priority` (int), `tech_stack`, `category`, `key_features`, and optionally `live`. Sorted by `priority` at init time via `sorted(..., key=lambda p: p["priority"])`. To reorder projects, change the `priority` values.
- `self.cloud_skills`, `self.languages` — skill metadata used in `generate_report()` and `get_skills_by_category()`
- `self.availability` — computed by `_check_availability()` based on current month; controls status messaging in `say_hi()`

**Key methods:**
- `say_hi()` — greeting + random featured project + availability status
- `recommend_project(interest)` — keyword-matches interest string to one of four starter repos
- `get_repository_stats()` — calls GitHub API, returns repos sorted by stars descending with a `repos_by_stars` ranked list
- `generate_report()` / `to_json()` / `save_profile()` — output formatters

**Optional deps** are guarded with try/except at the top; `COLORS_ENABLED` and `REQUESTS_ENABLED` flags control feature availability gracefully.

## Keeping README.md and github_profile.py in sync

`README.md` is the public-facing profile; `github_profile.py` is the programmatic version. When adding or removing projects, update both files. The project order in `README.md` should reflect the `priority` order in `github_profile.py`.

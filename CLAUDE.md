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
python github_profile.py --report                 # formatted full profile report
python github_profile.py --save json              # save profile to JSON file
python github_profile.py --chat                   # AI chat mode (requires ANTHROPIC_API_KEY)
```

Install dependencies:
```bash
pip install rich requests anthropic
```

For `--chat`: export `ANTHROPIC_API_KEY` before running. Uses `claude-haiku-4-5-20251001` with streaming and multi-turn history.

## Architecture of github_profile.py

Single-file, single-class design — `AIBuilder` holds all profile data and logic.

**Data** is declared in `__init__`:
- `self.projects` — list of project dicts, each with `priority` (int), `tech_stack`, `category`, `key_features`, and optionally `live`. Sorted by `priority` at init time via `sorted(..., key=lambda p: p["priority"])`. To reorder projects, change the `priority` values.
- `self.cloud_skills`, `self.languages` — skill metadata used in `generate_report()` and `get_skills_by_category()`
- `self.availability` — computed by `_check_availability()` based on current month; controls status messaging in `say_hi()`

**Key methods:**
- `print_greeting()` — rich panels: greeting + random featured project + availability side-by-side
- `recommend_project(interest)` / `print_recommendation()` — keyword-matches interest to one of four starter repos, renders as a rich table
- `get_repository_stats()` / `print_stats()` — calls GitHub API, returns repos sorted by stars descending
- `print_report()` — full rich report: language/cloud tables + all projects + availability
- `chat()` — interactive multi-turn AI chat using Claude (streaming), grounded in `_build_system_prompt()` which serialises the full profile into a system prompt
- `to_json()` / `save_profile()` — output serialisers

**Optional deps:** `requests` guarded by `REQUESTS_ENABLED`; `anthropic` by `ANTHROPIC_ENABLED`. Both degrade gracefully with a rich error panel. `rich` is a hard dependency now.

## GitHub Actions

`.github/workflows/update-readme.yml` — runs weekly (Mondays 07:00 UTC) and on every push to `main`. Fetches live repo stats via the GitHub API and injects/updates a badge block between `<!-- stats-start -->` and `<!-- stats-end -->` markers in `README.md`, then commits with `[skip ci]`.

## Keeping README.md and github_profile.py in sync

`README.md` is the public-facing profile; `github_profile.py` is the programmatic version. When adding or removing projects, update both files. The project order in `README.md` should reflect the `priority` order in `github_profile.py`.

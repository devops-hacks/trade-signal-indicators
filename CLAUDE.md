# CLAUDE.md — Claude Code project instructions

## Project Overview

Trading Signals — a collection of Python scripts that generate visual examples of
trading indicators (price charts paired with signal/indicator overlays). Currently
stand-alone analysis scripts; may evolve into a web-based app in the future.

## Tech Stack

- **Language:** Python 3.12+
- **Dependency management:** Poetry (package-mode = false, scripts-only project)
- **Linting / formatting:** Ruff
- **Type checking:** pyright
- **Testing:** pytest

## Commands

All commands should be run via `poetry run` to ensure the virtual environment is used.

```bash
# Install dependencies (also creates .venv if missing)
poetry install

# Run a script
poetry run python RSI/divergence_signal.py

# Lint + auto-fix
poetry run ruff check --fix .

# Format
poetry run ruff format .

# Type check
poetry run pyright

# Run tests
poetry run pytest

# Run tests with verbose output + coverage
poetry run pytest -v --cov

# Add a new dependency
poetry add <package>

# Add a new dev dependency
poetry add --group dev <package>
```

## Code Style

- Follow Ruff defaults (equivalent to Black + isort + flake8).
- Target Python 3.12 features — use modern syntax (match/case, type unions with `|`, etc.).
- Use type hints on all function signatures. Use `pyright`-compatible syntax.
- Max line length: 88 (Ruff default).
- Prefer f-strings over `.format()` or `%` formatting.
- Import ordering is handled automatically by Ruff — don't manually separate stdlib/third-party/local imports.

## Project Structure

```
├── RSI/                        # RSI indicator scripts
│   └── divergence_signal.py
├── tests/                      # pytest test files (mirror source layout)
│   └── ...
├── pyproject.toml              # Poetry config, dependencies, tool settings
├── CLAUDE.md                   # This file — Claude Code instructions
└── README.md                   # Quick start for new developers
```

Conventions:
- Each indicator gets its own top-level directory (e.g., `RSI/`, `MACD/`).
- Scripts that produce visual output should save images to an `output/` directory (gitignored).
- Test files go in `tests/` mirroring the source layout (e.g., `tests/RSI/test_divergence_signal.py`).

## Development Workflow — Test-Driven Development (TDD)

**Always ask questions first.** Before writing any code or tests, clarify:

- What exactly is the feature/requirement?
- What test approach is appropriate for this feature (unit, integration, property-based)?
- Are there edge cases or scenarios the user wants covered?
- Should this use TDD, BDD, or a combination?

### TDD First (default for all new features)

Follow the Red → Green → Refactor cycle strictly:

1. **Red** — Write a failing test that describes the desired behavior. Do NOT write any implementation code yet.
   - The test must fail for the right reason (i.e., the feature doesn't exist yet, not a syntax error).
   - Commit the failing test.

2. **Green** — Write the minimum code needed to make the test pass. No extra logic, no gold-plating.
   - Run the test to confirm it passes.
   - Commit the passing implementation.

3. **Refactor** — Clean up both the test and implementation code while keeping all tests green.

### BDD for higher-level features

For user-facing features or multi-step workflows, supplement TDD with BDD:

- Use Given-When-Then structure in test names or docstrings.
- Focus on behavior and outcomes, not implementation details.
- Example: `test_given_bullish_divergence_when_rsi_crosses_50_then_signal_is_generated`.

### Key rules

- **Never write implementation before a failing test exists.** If unclear what to test, ask first.
- **One test → one small piece of behavior.** Don't write a massive test suite upfront.
- **Tests drive the design.** If a feature is hard to test, the design needs rethinking — ask about it.
- **Commit after each Red-Green-Refactor cycle** to preserve the TDD history.

## Testing Guidelines

- Use pytest. Test files named `test_*.py` or `*_test.py`.
- Place tests in `tests/` mirroring the source directory structure.
- Each test function should be self-contained — don't rely on shared mutable state.
- Use descriptive test names that describe the expected behavior: `test_bullish_divergence_detects_higher_low_in_rsi`.
- For data-heavy tests, use small fixed fixtures rather than reading from disk.
- Avoid mocking unless testing external API boundaries.

## Git Conventions

- Commit messages: short imperative summary, optionally a body with context.
- Keep commits small and focused on a single concern.
- Don't commit generated output (images, data files), only source code.

## Adding a New Indicator Script (TDD)

1. Ask questions to clarify the feature and test approach before writing anything.
2. Create a new directory: `mkdir <INDICATOR>/`
3. Create the test file first: `tests/<INDICATOR>/test_<script_name>.py`
4. Write a failing test (Red phase), run `poetry run pytest` to confirm it fails.
5. Write the minimum implementation in `<INDICATOR>/<script_name>.py` to pass the test (Green phase).
6. Refactor both test and implementation while keeping tests green (Refactor phase).
7. Install any new dependencies: `poetry add <package>`
8. Run lint + type check + tests before committing.

---

## Optional — Uncomment if/when needed

# ## Web Application
#
# When the project evolves into a web app, consider:
# - Framework: FastAPI or Flask
# - Add as dependencies: `poetry add fastapi uvicorn` or `poetry add flask`
# - Move scripts into an `app/` package with proper `__init__.py`
# - Add API routes or page views for navigating indicator examples
# - Static assets (images, CSS, JS) go in `app/static/`
# - Templates go in `app/templates/` (if using server-side rendering)

# ## CI/CD
#
# Recommended GitHub Actions workflow (.github/workflows/ci.yml):
# - Trigger on push to main and pull requests
# - Steps: checkout, setup Python 3.12, install Poetry, run `poetry install`,
#   run `ruff check .`, run `pyright`, run `pytest --cov`
# - Fail the build if any step fails

# ## Pre-commit Hooks
#
# Install pre-commit to auto-run checks before every commit:
#   poetry add --group dev pre-commit
#   pre-commit install
#
# Add a .pre-commit-config.yaml with:
#   - ruff (lint + format)
#   - pyright (type check)

# ## Environment Variables
#
# If the project needs env vars (API keys, config), use a .env file:
# - Add `python-dotenv` as a dependency: `poetry add python-dotenv`
# - Create `.env.example` with placeholder values (committed to repo)
# - Add `.env` to .gitignore (already excluded via *. patterns)

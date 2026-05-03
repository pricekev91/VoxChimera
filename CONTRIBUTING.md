# Contributing to VoxChimera

Thank you for your interest in contributing!  VoxChimera is currently in an
exploratory phase, so the bar for contribution is intentionally low — all you
need is Python knowledge and an interest in LLM-driven narration.

---

## 1. Clone and Run Locally

```bash
git clone https://github.com/pricekev91/VoxChimera.git
cd VoxChimera

# Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the entry point
python src/main.py

# Run the test suite
pytest tests/
```

---

## 2. Branching Model

| Branch | Purpose |
|---|---|
| `main` | Stable, releasable code |
| `feature/<name>` | New features or experiments |
| `fix/<name>` | Bug fixes |
| `docs/<name>` | Documentation-only changes |

All changes must be submitted via a pull request targeting `main`.
Squash-merge is the preferred strategy to keep the commit history readable.

---

## 3. Conventional Commits

Commit messages must follow the
[Conventional Commits](https://www.conventionalcommits.org/) specification:

```
<type>(<optional scope>): <short description>

[optional body]

[optional footer(s)]
```

### Allowed Types

| Type | When to use |
|---|---|
| `feat` | A new feature |
| `fix` | A bug fix |
| `docs` | Documentation only |
| `refactor` | Code change that neither fixes a bug nor adds a feature |
| `test` | Adding or updating tests |
| `chore` | Build process, tooling, dependency updates |
| `perf` | Performance improvements |

### Examples

```
feat(orchestrator): add LangChain backend adapter
fix(audio): handle empty bytes from TTS stub
docs(decisions): add ADR 003 for TTS engine selection
```

---

## 4. Code Style Expectations

- **Python version**: 3.11+
- **Formatter**: `black` (line length 88)
- **Import sorter**: `isort` (compatible with black)
- **Type hints**: required for all public functions and methods
- **Docstrings**: Google style, required for all public APIs
- **No magic**: prefer explicit over implicit; avoid metaclasses,
  monkey-patching, or framework magic unless absolutely necessary

Run the linters before opening a PR:

```bash
black src/ tests/
isort src/ tests/
```

---

## 5. ADR Workflow

Any significant architectural decision must be captured as an ADR in
[`docs/decisions.md`](docs/decisions.md) before the implementation lands.

1. Copy the ADR template from the top of `docs/decisions.md`.
2. Assign the next sequential number.
3. Fill in Context, Decision, and Consequences.
4. Submit the ADR as part of the same PR as the implementation, or as a
   preceding PR if the decision needs review before coding begins.

---

## 6. Questions

Open a GitHub Issue with the `question` label, or start a Discussion.

# Architecture Decision Records — VoxChimera

This file tracks significant architectural decisions made during the development
of VoxChimera using a lightweight ADR (Architecture Decision Record) format.

---

## ADR Template

```
## ADR NNN: <Title>

| Field  | Value |
|--------|-------|
| Status | Proposed / Accepted / Deprecated / Superseded |
| Date   | YYYY-MM-DD |
| Author | <name or handle> |

### Context
<What situation prompted this decision?>

### Decision
<What was decided?>

### Consequences
<What are the trade-offs, risks, or follow-on actions?>
```

---

## ADR 001: Why this project is isolated in its own repository

| Field  | Value |
|--------|-------|
| Status | Accepted |
| Date   | 2026-05-03 |
| Author | pricekev91 |

### Context

The author maintains three separate projects: **TrashPandaOmega**,
**BrickCipher**, and **VoxChimera**.  Each targets a different domain and is
at a different stage of development.  There is no functional overlap between
them, and their dependency graphs, release cadences, and contributor audiences
are expected to diverge significantly over time.

Placing all three in a monorepo would create hidden coupling risks, complicate
dependency management, pollute each project's issue tracker, and introduce
tooling complexity (workspace scripts, cross-project CI, shared changelogs)
that delivers no benefit in return.

### Decision

VoxChimera lives in its own dedicated GitHub repository with its own
dependencies, CI pipeline, changelog, and release tags.  It shares **no**
code, configuration, or CI resources with TrashPandaOmega or BrickCipher.

### Consequences

- **Positive**: full autonomy over dependency versions and release schedule.
- **Positive**: issues, PRs, and changelogs are scoped to this project only.
- **Positive**: onboarding is simple — clone this one repo and you have
  everything you need.
- **Trade-off**: any utility code that genuinely generalises across projects
  must be extracted into a standalone published package rather than imported
  from a sibling directory.  This is an acceptable cost and enforces cleaner
  abstraction boundaries.

---

## ADR 002: Initial technology stack selection (Python + LLM frameworks)

| Field  | Value |
|--------|-------|
| Status | Accepted |
| Date   | 2026-05-03 |
| Author | pricekev91 |

### Context

VoxChimera's primary concerns are:

1. LLM inference and orchestration (prompt engineering, chaining, tool use).
2. Text-to-speech audio synthesis.
3. Glue logic connecting the two pipelines.

A language and toolchain must be chosen that offers mature libraries in both
domains, is well-understood by the author, and keeps the stack simple during
an exploratory "vibe coding" phase.

### Decision

- **Primary language**: Python 3.11+
- **LLM orchestration**: LangChain or LlamaIndex (final choice deferred until
  integration work begins; the orchestrator is hidden behind an abstract
  interface so the backend can be swapped without touching callers).
- **Audio synthesis**: TTS engine TBD (candidates: Coqui TTS for fully local
  inference; ElevenLabs SDK for hosted high-quality voices).
- **Testing**: `pytest` — minimal, widely adopted, no special plugins required
  for the current stub-only test suite.
- **Packaging**: `pip` + `requirements.txt` initially; migrate to
  `pyproject.toml` when the dependency graph stabilises.

### Consequences

- **Positive**: Python has first-class support in every major LLM and TTS
  library; no FFI or bridge layer needed.
- **Positive**: the abstract orchestrator interface allows the LLM backend to
  be changed without breaking the text or audio pipelines.
- **Trade-off**: Python's performance ceiling may require careful chunking
  strategies for long-form narration; this is a known and accepted constraint.
- **Trade-off**: deferring the final TTS engine selection means the audio
  pipeline stub must remain generic; any engine-specific features (voice
  cloning, emotion tags) cannot be designed in until the decision is made.
- **Follow-on**: open a new ADR when the TTS engine is selected.
- **Follow-on**: open a new ADR when the LLM backend is finalised.

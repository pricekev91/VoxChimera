# VoxChimera

> Multimodal narration + LLM orchestration.

VoxChimera is an exploratory Python project focused on combining large language model (LLM) orchestration with audio-driven narration pipelines. The goal is to build a modular, reproducible system that can ingest text, process it through LLM-based reasoning, and emit high-quality synthesized narration — cleanly separated from the rest of the author's project ecosystem (TrashPandaOmega, BrickCipher).

---

## Key Features

- **Text pipeline** — preprocessing, chunking, and prompt engineering for LLM input
- **Audio pipeline** — text-to-speech synthesis and audio post-processing
- **LLM orchestrator** — pluggable backend supporting multiple LLM frameworks
- **Modular architecture** — each pipeline component is independently testable
- **Explicit boundaries** — no shared code or dependencies with sibling projects
- **Reproducible environments** — pinned dependencies and deterministic builds

---

## Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.11+ |
| LLM Frameworks | LangChain / LlamaIndex (TBD) |
| Audio Tools | TTS engine TBD (e.g., Coqui TTS, ElevenLabs SDK) |
| Testing | pytest |
| Packaging | pip + `requirements.txt` / `pyproject.toml` |

---

## Getting Started

### Prerequisites

- Python 3.11+
- `git`

### Clone & Run

```bash
git clone https://github.com/pricekev91/VoxChimera.git
cd VoxChimera
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python src/main.py
```

### Run Tests

```bash
pytest tests/
```

---

## Folder Structure

```
VoxChimera/
├── src/                  # Application source code
│   └── main.py           # Entry point
├── tests/                # Pytest test suite
│   └── test_main.py
├── docs/                 # Project documentation
│   ├── architecture.md   # System design overview
│   └── decisions.md      # Architecture Decision Records (ADRs)
├── scripts/              # Automation scripts
├── .gitignore
├── CHANGELOG.md
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── LICENSE
└── README.md
```

---

## Versioning Strategy

VoxChimera follows [Semantic Versioning](https://semver.org/) (`MAJOR.MINOR.PATCH`):

- **MAJOR** — breaking changes to public APIs or core behavior
- **MINOR** — new backward-compatible features
- **PATCH** — bug fixes and small improvements

All notable changes are recorded in [CHANGELOG.md](CHANGELOG.md).

---

## Branching Model

| Branch | Purpose |
|---|---|
| `main` | Stable, releasable code |
| `feature/<name>` | New features or experiments |
| `fix/<name>` | Bug fixes |
| `docs/<name>` | Documentation-only changes |

Pull requests target `main`. Squash-merge is preferred to keep history clean.

---

## Roadmap

> _This section will be populated as the project matures._

- [ ] Core text pipeline implementation
- [ ] LLM orchestrator (first backend)
- [ ] Audio synthesis integration
- [ ] CLI entry point
- [ ] Streaming narration support
- [ ] Evaluation / quality metrics

---

## Philosophy

VoxChimera is built on a few guiding principles:

- **Modularity** — components should be replaceable and independently testable.
- **Explicitness** — prefer explicit configuration and interfaces over implicit magic.
- **Reproducibility** — environments and builds must be deterministic.
- **Clean boundaries** — this project shares nothing with TrashPandaOmega or BrickCipher.
- **Future-proof scaffolding** — invest in structure early, even during exploratory phases.

---

## License

[MIT](LICENSE)

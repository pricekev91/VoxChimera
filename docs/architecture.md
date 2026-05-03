# VoxChimera — Architecture

> Status: **Draft** (initial scaffold)  
> Last updated: 2026-05-03

---

## 1. High-Level System Overview

VoxChimera is a multimodal narration system that transforms text input into
synthesised audio narration via a language model.  The system is composed of
three loosely-coupled pipeline stages:

```
┌─────────────┐     ┌──────────────────┐     ┌─────────────────┐
│  Text Input │────▶│  Text Pipeline   │────▶│ LLM Orchestrator│
│  (raw text, │     │  (preprocess,    │     │ (prompt, infer, │
│   prompts)  │     │   chunk, template│     │  post-process)  │
└─────────────┘     └──────────────────┘     └────────┬────────┘
                                                       │
                                                       ▼
                                             ┌─────────────────┐     ┌────────────┐
                                             │  Audio Pipeline │────▶│ Audio Out  │
                                             │  (TTS synth,    │     │ (file/stream)
                                             │   post-process) │     └────────────┘
                                             └─────────────────┘
```

---

## 2. Core Components

### 2.1 Text Pipeline (`src/pipeline/text.py` — TODO)

Responsible for:

- Ingesting raw text or structured prompts
- Tokenisation and length-aware chunking
- Prompt template rendering
- Passing processed chunks to the LLM orchestrator

### 2.2 LLM Orchestrator (`src/orchestrator/llm.py` — TODO)

Responsible for:

- Abstracting over multiple LLM backends (LangChain, LlamaIndex, direct API)
- Prompt construction and injection
- Response parsing and post-processing
- Rate-limiting and retry logic

### 2.3 Audio Pipeline (`src/pipeline/audio.py` — TODO)

Responsible for:

- Accepting LLM-generated text
- Invoking the configured TTS engine
- Post-processing audio (normalisation, pacing)
- Outputting bytes to a file or streaming endpoint

---

## 3. Data Flow Description

1. The caller passes raw text to `run_text_pipeline()`.
2. The text pipeline preprocesses, chunks, and templates the input.
3. Each chunk is forwarded to `run_llm_orchestrator()`.
4. The orchestrator constructs a full prompt, calls the backend, and returns
   a structured response.
5. The response text is passed to `run_audio_pipeline()`.
6. The audio pipeline synthesises speech and returns raw audio bytes.
7. The caller writes the bytes to a file or streams them to a playback device.

---

## 4. Dependencies and Integration Points

| Component | External Dependency | Notes |
|---|---|---|
| LLM Orchestrator | LangChain or LlamaIndex | TBD — see ADR 002 |
| Audio Pipeline | Coqui TTS / ElevenLabs SDK | TBD — evaluated in roadmap |
| Config | `pydantic-settings` or plain dataclasses | Keep minimal |
| Testing | `pytest` | No extras required for stubs |

---

## 5. Assumptions and Constraints

- **Python 3.11+** is the minimum runtime.
- The system is designed for **batch** narration first; real-time streaming is
  a future concern.
- **No shared code** with TrashPandaOmega or BrickCipher.
- LLM backend is **pluggable** via an abstract interface — no vendor lock-in.
- Audio engine selection is deferred; the pipeline interface is stable.

---

## 6. Security Considerations

- API keys for LLM services must be loaded from environment variables or a
  secrets manager — never hardcoded or committed.
- Audio output files should be written to a sandboxed output directory with
  validated filenames to prevent path traversal.
- Prompt injection risks should be mitigated by sanitising user-supplied text
  before it is inserted into prompt templates.

---

## 7. Future Expansion Notes

- **Streaming narration**: chunk-by-chunk audio output for lower latency.
- **Multi-voice support**: assign different voices to different speakers or
  narrative roles.
- **Evaluation harness**: automated quality scoring of LLM outputs and audio
  fidelity.
- **Plugin system**: allow third-party pipeline stages to be registered without
  modifying core code.

---

## 8. Text-Based Diagram Description

```
User / Caller
     │
     │  raw text / prompt
     ▼
┌──────────────────────────────────────────────────────────────────┐
│                        VoxChimera Core                           │
│                                                                  │
│  ┌─────────────────┐   chunks   ┌──────────────────────────┐    │
│  │  Text Pipeline  │──────────▶│    LLM Orchestrator       │    │
│  │  - tokenise     │            │  - prompt construction    │    │
│  │  - chunk        │            │  - backend call           │    │
│  │  - template     │            │  - response parsing       │    │
│  └─────────────────┘            └──────────────┬───────────┘    │
│                                                │ response text  │
│                                                ▼                │
│                                 ┌──────────────────────────┐    │
│                                 │    Audio Pipeline         │    │
│                                 │  - TTS synthesis          │    │
│                                 │  - audio post-processing  │    │
│                                 └──────────────┬────────────┘   │
└──────────────────────────────────────────────┬─┘               │
                                               │ audio bytes      │
                                               ▼
                                        File / Stream
```

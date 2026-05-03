"""
Placeholder tests for VoxChimera's core pipeline functions.

These tests verify the stub behaviour of the initial scaffold.  As real
implementations replace the placeholders, update or expand the assertions
accordingly.
"""

from __future__ import annotations

import pytest

from src.main import run_audio_pipeline, run_llm_orchestrator, run_text_pipeline


# ---------------------------------------------------------------------------
# Text pipeline
# ---------------------------------------------------------------------------


def test_text_pipeline_returns_string() -> None:
    result = run_text_pipeline("hello world")
    assert isinstance(result, str)


def test_text_pipeline_passthrough() -> None:
    """Stub should return input unchanged until chunking is implemented."""
    sample = "Some raw narration text."
    assert run_text_pipeline(sample) == sample


# ---------------------------------------------------------------------------
# LLM orchestrator
# ---------------------------------------------------------------------------


def test_llm_orchestrator_returns_string() -> None:
    result = run_llm_orchestrator("test prompt")
    assert isinstance(result, str)


def test_llm_orchestrator_non_empty() -> None:
    result = run_llm_orchestrator("What is VoxChimera?")
    assert len(result) > 0


# ---------------------------------------------------------------------------
# Audio pipeline
# ---------------------------------------------------------------------------


def test_audio_pipeline_returns_bytes() -> None:
    result = run_audio_pipeline("Narrate this.")
    assert isinstance(result, bytes)


# ---------------------------------------------------------------------------
# TODO: add integration tests once real pipeline components are in place.
# ---------------------------------------------------------------------------

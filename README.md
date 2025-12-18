# Healthcare API Enhancer

A flagship **MLOps-focused backend project** demonstrating how to design and version
a production-ready ML inference API — with emphasis on **model lifecycle, correctness,
and release discipline**, not just model training.

This is **not a CRUD app** and **not a notebook demo**.

---

## Project Goals

- Show how ML models are **loaded, managed, and served** in a real API
- Follow **production-style Git workflows** (branches, releases, tags)
- Build incrementally with **truthful, runnable releases**

---

## Current Status

**Latest release:** `v0.2.0`

What exists today:
- FastAPI service with health check
- Explicit ML model lifecycle (startup loading)
- In-memory model state management
- `/predict` endpoint scaffold with validated request/response schemas

What does **not** exist yet (by design):
- model training
- database
- authentication
- deployment
- UI/dashboard

---

## Architecture Overview

High-level structure:
- **FastAPI** application
- Model loaded once at startup via lifecycle hooks
- Model stored in application state and reused across requests
- Inference endpoint consumes the loaded model

Detailed architecture decisions live in [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md).

---

## Versioning Philosophy

Releases represent **truthful checkpoints**, not feature completeness.

Each version answers:
> *“What reliably works right now?”*

See the **Releases** page for version-by-version progression.

---

## License

MIT

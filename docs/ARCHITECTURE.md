# Architecture — Healthcare API Enhancer

This document explains the **current system architecture** and the reasoning
behind key design decisions.

It reflects the state of the system as of **v0.3.0**.

---

## High-Level Overview

The Healthcare API Enhancer is a **backend ML inference service** built using FastAPI.

The system is designed around one core principle:

> **Model lifecycle must be explicit, predictable, and independent of request handling.**

---

## Core Components

### API Layer
- Framework: FastAPI
- Entry point: `backend/app/main.py`
- Responsibilities:
  - application startup
  - routing
  - lifecycle orchestration

---

### Model Lifecycle

The ML model lifecycle is intentionally separated into three concerns:

#### 1. Model Creation
File:
- `backend/app/ml/loader.py`

Responsibility:
- Load and return a model object
- No awareness of FastAPI or request handling

This allows the model source to change later
(file, registry, cloud storage) without affecting the API.

---

#### 2. Model State
File:
- `backend/app/ml/state.py`

Responsibility:
- Hold the currently loaded model in memory
- Provide controlled access via getter/setter functions

A lightweight dataclass defines the shape of application state.
The state object stores a **reference** to the model, not the model logic itself.

---

#### 3. Lifecycle Timing
File:
- `backend/app/main.py`

Responsibility:
- Load the model once at application startup
- Fail fast if loading fails
- Ensure all requests reuse the same model instance

FastAPI’s lifespan mechanism is used to guarantee correct timing.

---

## Observability (Minimal, Intentional)

As of v0.3.0, observability is intentionally lightweight:
- file-based JSONL logging
- privacy-safe metadata only (no raw input text)
- request-level correlation via request_id
- latency measurement for performance insight

This establishes an observability foundation
without introducing premature infrastructure.

---

## Inference Flow (Post v0.3.0)

1. Application starts
2. Model is loaded once during startup (FastAPI lifespan)
3. Model is stored in application state
4. Requests arrive at `/predict`
5. Input is validated and normalized at the schema layer
6. Request-level instrumentation is applied:
   - request_id generated
   - high-resolution latency timer started
7. Endpoint retrieves the already-loaded model from state
8. Prediction is generated (placeholder at this stage)
9. A PII-safe prediction event is logged
10. Response is returned to the client

The model is **never loaded per request**.

---

## `/predict` Endpoint (Current Scope)

- Endpoint: `POST /predict`
- Uses validated request and response schemas
- Returns a placeholder prediction
- Confirms correct lifecycle wiring

No real ML inference logic is included yet.

As of v0.3.0, the endpoint additionally includes:
- schema-level input validation and normalization
- request_id generation
- latency measurement
- PII-safe prediction logging (file-based, JSONL)

---

## Out-of-Scope (By Design)

As of v0.3.0, the system intentionally does not include:
- model training pipelines
- databases or persistence layers
- caching beyond local memory
- authentication or authorization
- frontend UI or dashboards
- Docker or cloud deployment configuration
- MLflow or drift monitoring

These will be introduced incrementally in future releases.

---

## Architectural Principles

- Explicit lifecycle over hidden globals
- Separation of concerns over convenience
- Small, truthful releases over premature complexity
- Infrastructure before intelligence

---

## Versioning

Architecture evolves incrementally.
Each release documents what the system **can reliably do at that point in time**.

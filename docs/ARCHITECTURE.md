# Architecture — Healthcare API Enhancer

This document explains the **current system architecture** and the reasoning
behind key design decisions.

It reflects the state of the system as of **v0.2.0**.

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

## Inference Flow

1. Application starts
2. Model is loaded once during startup
3. Model is stored in application state
4. Requests arrive at `/predict`
5. Endpoint retrieves the already-loaded model from state
6. Response is returned

The model is **never loaded per request**.

---

## `/predict` Endpoint (Current Scope)

- Endpoint: `POST /predict`
- Uses validated request and response schemas
- Returns a placeholder prediction
- Confirms correct lifecycle wiring

No training or inference logic is included yet.

---

## Out-of-Scope (By Design)

As of v0.2.0, the system intentionally does not include:
- model training pipelines
- databases or persistence
- logging or monitoring
- caching
- authentication
- deployment configuration

These are planned for future incremental releases.

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

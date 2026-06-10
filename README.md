# Mental Health Care Prototype

This repository contains a prototype Mental Health Care application built as part of the MHC project. It combines a FastAPI backend with a simple frontend user interface to support patient registration, lookup, and workflow validation for an infant and maternal healthcare context.

## Overview

- Backend: `FastAPI` application in `prototype-backend/app/`
- Frontend: static UI pages in `prototype-backend/frontend/`
- Database: prototype SQLite datastore at `prototype-backend.db`
- Tests: API tests in `prototype-backend/tests/`

## Key features

- Patient registration form with data validation
- Search patients by name or National Health Identifier (NHI)
- Serve frontend and backend from a single FastAPI app
- Interactive API documentation available at `/api/docs`

## Getting started

1. Navigate to the project folder:
   ```bash
   cd prototype-backend
   ```

2. Create and activate a Python virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   ./run.sh
   ```

5. Open the app in your browser:
   - Frontend UI: `http://localhost:8000/`
   - API docs: `http://localhost:8000/api/docs`

## Repository structure

- `prototype-backend/app/` — FastAPI backend code and data models
- `prototype-backend/frontend/` — simple client UI
- `prototype-backend/tests/` — automated API tests
- `prototype-backend/requirements.txt` — Python dependencies
- `prototype-backend/run.sh` — launch script for the prototype server
- `prototype-backend.db` — SQLite prototype datastore
- `SRS_extracted.txt` / `SRS_Mental_Infant_Healthcare_Cameroon.docx` — requirements and system specification artifacts

## Notes

This repository is intended as an initial prototype for a mental health and infant healthcare information management system (IMHIHMS). It is a starting point for adding secure user authentication, extended patient modules, offline support, and integration with national health systems.

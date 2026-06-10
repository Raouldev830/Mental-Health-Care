Prototype IMHIHMS backend + frontend prototype

This prototype implements a FastAPI backend API and a simple professional frontend UI for patient registration and search.

Quick start:

1. Create a virtual environment and install dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2. Run the server:

```bash
./run.sh
```

3. Open the app in your browser:

- http://localhost:8000/  (frontend user interface)
- http://localhost:8000/api/docs  (interactive API docs)

Project structure:

- `app/` — FastAPI backend code and API endpoints
- `frontend/` — client-side UI served by FastAPI
- `tests/` — API tests

Frontend highlights:

- patient registration form with validation
- search by name or NHI
- responsive layout and clean UI styling

Next steps: add immunisation and growth modules, offline sync, authentication, and DHIS2 export.

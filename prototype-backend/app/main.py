import os
import uuid
from datetime import date

from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from sqlmodel import select

from app.database import get_session, init_db
from app.models import Patient

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
FRONTEND_DIR = os.path.join(BASE_DIR, "frontend")

app = FastAPI(
    title="IMHIHMS Prototype API",
    docs_url="/api/docs",
    openapi_url="/api/openapi.json",
)

app.mount("/static", StaticFiles(directory=FRONTEND_DIR), name="static")

@app.get("/", response_class=HTMLResponse)
def frontend_root():
    return FileResponse(os.path.join(FRONTEND_DIR, "index.html"))

@app.get("/api")
def api_root():
    return {
        "message": "IMHIHMS Prototype API running",
        "frontend": "/",
        "docs": "/api/docs",
    }

@app.on_event("startup")
def on_startup():
    init_db()

@app.post('/patients', response_model=Patient)
def create_patient(payload: Patient):
    # basic duplicate check: same full_name & date_of_birth or same NHI
    # coerce date string to date object if necessary
    if isinstance(payload.date_of_birth, str):
        try:
            payload.date_of_birth = date.fromisoformat(payload.date_of_birth)
        except Exception:
            raise HTTPException(status_code=400, detail='Invalid date_of_birth format, expected YYYY-MM-DD')

    with get_session() as session:
        if payload.nhi:
            stmt = select(Patient).where(Patient.nhi == payload.nhi)
            existing = session.exec(stmt).first()
            if existing:
                raise HTTPException(status_code=400, detail='Patient with NHI already exists')

        stmt = select(Patient).where(
            Patient.full_name == payload.full_name,
            Patient.date_of_birth == payload.date_of_birth,
        )
        dup = session.exec(stmt).first()
        if dup:
            raise HTTPException(status_code=400, detail='Potential duplicate patient found')

        if not payload.nhi:
            payload.nhi = 'NHI-' + uuid.uuid4().hex[:10].upper()

        session.add(payload)
        session.commit()
        session.refresh(payload)
        return payload

@app.get('/patients')
def search_patients(q: str = Query(None), limit: int = 20):
    with get_session() as session:
        stmt = select(Patient)
        if q:
            # simple search across name and nhi
            stmt = select(Patient).where(
                (Patient.full_name.ilike(f"%{q}%")) | (Patient.nhi.ilike(f"%{q}%")),
            )
        results = session.exec(stmt).all()
        return results[:limit]

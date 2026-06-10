from typing import Optional
from sqlmodel import SQLModel, Field
from datetime import date

class Patient(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nhi: Optional[str] = Field(default=None, index=True)
    full_name: str
    date_of_birth: date
    sex: Optional[str] = None
    region: Optional[str] = None
    district: Optional[str] = None
    contact: Optional[str] = None

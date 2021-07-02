from datetime import date
from typing import Optional
from pydantic import BaseModel

class User(BaseModel):
    user_id: Optional[int] = None
    birth: Optional[date] = None
    codigo_postal: Optional[str] = None
    address_user: Optional[str] = None
    country: Optional[str] = None
    email: Optional[str] = None
    first_name: Optional[str] = None
    gender: Optional[str] = None
    last_name: Optional[str] = None
    officialdocument: Optional[str] = None
    officialdocument2: Optional[str] = None
    password_user: Optional[str] = None
    proofofaddress: Optional[str] = None
    user_type: Optional[str] = None

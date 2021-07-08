from datetime import date
from typing import Optional
from pydantic import BaseModel

class Categories(BaseModel):
    user_id: Optional[int] = None
    birth: Optional[str] = None

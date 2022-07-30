from datetime import datetime
from sqlite3 import Timestamp
from pydantic import BaseModel, EmailStr
from typing import List


class UserBase(BaseModel):
    email: EmailStr
    password: str

class UserDisplay(BaseModel):
    email:str

    class Config():
        orm_mode = True
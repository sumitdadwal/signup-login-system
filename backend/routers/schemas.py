from datetime import datetime
from sqlite3 import Timestamp
from pydantic import BaseModel
from typing import List


class UserBase(BaseModel):
    email: str
    password: str

class UserDisplay(BaseModel):
    email:str

    class Config():
        orm_mode = True
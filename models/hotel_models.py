from pydantic import BaseModel

class HotelIn(BaseModel):
    mail: str
    password: str

class HotelOut(BaseModel):
    mail: str
    name: str
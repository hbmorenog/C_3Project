from typing import Dict
from pydantic import BaseModel
from models.hotel_models import HotelOut
class HotelInDB(BaseModel):
    mail: str
    password: str
    ubication: str
    name: str
    price: int 

database_hotel= Dict[str, HotelInDB]

database_hotel={
    "decameron@gmail.com": HotelInDB(**{"mail":"decameron@gmail.com",
                    "password":"123abc",
                    "ubication":"Cartagena",
                    "name":"Decameron",
                    "price":250000}),
    "hilton@gmail.com": HotelInDB(**{"mail":"hilton@gmail.com",
                    "password":"root",
                    "ubication":"Santa Marta",
                    "name":"Hilton",
                    "price":300000}),
    "calypso@gmail.com": HotelInDB(**{"mail":"calypso@gmail.com",
                    "password":"admin123",
                    "ubication":"San Andres",
                    "name":"Calypso Beach",
                    "price":280000}),

}

def get_Hotel(mail:str):
    if mail in database_hotel.keys():
        return database_hotel[mail]
    else:
        return None

def update_hotel(hotel_in_db : HotelInDB):
    database_hotel[hotel_in_db.mail] = hotel_in_db
    return hotel_in_db


from pydantic import BaseModel


class HotelInDB(BaseModel):
    email: str
    password: str
    ubication: str
    name: str
    price: int 


database_hotel={
    "decameron@gmail.com": HotelInDB(email="decameron@gmail.com",
                    password="123abc",
                    ubication="Cartagena",
                    name="Decameron",
                    price=250000),
    "hilton@gmail.com": HotelInDB(id=2,email="hilton@gmail.com",
                    password="root",
                    ubication="Santa Marta",
                    name="Hilton",
                    price=300000),
    "calypso@gmail.com": HotelInDB(id=3,email="calypso@gmail.com",
                    password="admin123",
                    ubication="San Andres",
                    name="Calypso Beach",
                    price=280000)

}

def get_Hotels():
    lista_hoteles=[]
    for hotel in database_hotel:
        lista_hoteles.append(database_hotel[hotel])
    return lista_hoteles

def get_Hotel_email(email):
    if email in database_hotel:
        return database_hotel[email]
    else:
        return None

def enter_Hotel(hotel_add_db: HotelInDB):
    if hotel_add_db.email in database_hotel:
        return False
    else:
        database_hotel[hotel_add_db.email] = hotel_add_db
        return True

        

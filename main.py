from fastapi import FastAPI,HTTPException
from db import hotel_db
from modelos import modelo_hotel

app= FastAPI()

@app.get("/hoteles/resumen")
async def get_hoteles_api():
    return hotel_db.get_Hotels()

@app.post("/hotel")
async def auth_hotel(hotel_in: modelo_hotel.HotelIn): #mail query param
    hotel_in_db = hotel_db.get_Hotel_mail(hotel_in.mail)

    if hotel_in_db ==None:
        raise HTTPException(status_code=404,detail="El hotel no existe")
    
    if hotel_in_db.password != hotel_in.password:

        return {"Autenticado": False}

    return {"Autenticado": True}
    

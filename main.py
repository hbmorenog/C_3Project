from fastapi import FastAPI,HTTPException
from db import hotel_db

app= FastAPI()

@app.get("/hoteles/resumen")
async def get_hoteles_api():
    return contactos_db.get_Hotels()

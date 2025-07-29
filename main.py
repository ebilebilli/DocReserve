from fastapi import FastAPI

from db.base import Base
from db.session import engine
from doctors.models import Doctor
from apis.doctor_apis import router as doctor_router


app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(doctor_router)
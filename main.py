from fastapi import FastAPI
from db.base import Base
from db.session import engine
from doctors.models import Doctor


app = FastAPI()

Base.metadata.create_all(bind=engine)
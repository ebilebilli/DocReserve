from db.base import Base
from db.session import engine
from doctors.models import Doctor

Base.metadata.create_all(bind=engine)
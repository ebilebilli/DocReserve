from sqlalchemy import Column, Integer, String

from db.base import Base


class Doctor(Base):
    __tablename__ = "doctors"

    id = Column(
        Integer,
        primary_key=True, 
        index=True
    )
    full_name = Column(
        String, 
        nullable=False
    )
    age = Column(
        Integer, 
        nullable=True
    )
    specialization = Column(
        String, 
        nullable=False
    )
    experience = Column(
        Integer, 
        nullable=True,
    )
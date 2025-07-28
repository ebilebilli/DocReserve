from sqlalchemy import(
    Column, 
    Integer, 
    String,
    Boolean, 
    CheckConstraint
)

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
        nullable=True
    )
    about = Column(
        String,
        nullable=True
    )
    age = Column(
        Integer, 
        nullable=True,
    )
    specialization = Column(
        String, 
        nullable=True
    )
    experience = Column(
        Integer, 
        nullable=True,
    )
    is_active = Column(
        Boolean,
        default=True,
        nullable=False
    )

    __table_args__ = (
    CheckConstraint('age >= 18', name='check_age_limit'),
    CheckConstraint('experience >= 0', name='check_experience_positive'),
)

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from models import Doctor
from schemas import DoctorSchema


def get_doctor(db: Session, doctor_id: int):
    doctor = db.query(Doctor).filter(Doctor.id==doctor_id).first()
    return doctor


def get_doctors(db: Session):
    doctors = db.query(Doctor).filter(Doctor.is_active==True)
    return doctors


def create_doctor(db: Session, doctor: DoctorSchema):
    new_doctor = Doctor(
        full_name=doctor.full_name,
        about=doctor.about,
        age=doctor.age,
        specialization=doctor.specialization,
        experience=doctor.experience
    )
    db.add(new_doctor)
    db.commit()
    db.refresh(new_doctor)
    
    return new_doctor
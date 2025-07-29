from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from models import Doctor
from schemas import DoctorSchema


__all__ = [
    'get_doctor',
    'get_doctors',
    'create_doctor',
    'update_doctor',
    'delete_doctor'
]


def get_doctor(db: Session, doctor_id: int):
    doctor = db.query(Doctor).filter(Doctor.id==doctor_id).first()
    if not doctor:
        return HTTPException(status_code=404, detail='Doctor not found')
    
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


def update_doctor(db: Session,  doctor_id: int, doctor: DoctorSchema):
    existing_doctor = db.query(Doctor).filter(Doctor.id==doctor_id).first()
    if not existing_doctor:
        return HTTPException(status_code=404, detail='Doctor not found')
    
    existing_doctor.full_name=doctor.full_name,
    existing_doctor.about=doctor.about,
    existing_doctor.age=doctor.age,
    existing_doctor.specialization=doctor.specialization,
    existing_doctor.experience=doctor.experience
    db.commit()
    db.refresh(existing_doctor)

    return existing_doctor


def delete_doctor(db: Session, doctor_id: int):
    doctor = db.query(Doctor).filter(Doctor.id==doctor_id).first()
    db.delete(doctor)
    db.commit()

    return {'message': 'Doctor deleted successfully'}
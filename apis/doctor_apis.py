from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from db.session import get_db
from doctors.models import Doctor
from doctors.schemas import DoctorSchema
from doctors.cruds import *


router = APIRouter(
    prefix='/doctors',
    tags=['doctors']
)


@router.get('/', response_model=list[DoctorSchema], status_code=status.HTTP_200_OK)
def view_doctors(db: Session = Depends(get_db)):
    return get_doctors_crud(db)


@router.get('/{doctor_id}', response_model=DoctorSchema, status_code=status.HTTP_200_OK)
def view_doctor(doctor_id: int, db: Session=Depends(get_db)):
    return get_doctor_crud(db, doctor_id)
   

@router.post('/', response_model=DoctorSchema, status_code=status.HTTP_201_CREATED)
def create_new_doctor(doctor: DoctorSchema, db: Session = Depends(get_db)):
    return create_doctor_crud(db, doctor)


@router.patch('/{doctor_id}', response_model=DoctorSchema, status_code=status.HTTP_200_OK)
def update_doctor(doctor_id: int, doctor: DoctorSchema, db: Session = Depends(get_db)):
    return update_doctor_crud(db, doctor_id, doctor)


@router.delete('/{doctor_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_doctor(doctor_id: int, db: Session = Depends(get_db)):
    return delete_doctor_crud(db, doctor_id)
  
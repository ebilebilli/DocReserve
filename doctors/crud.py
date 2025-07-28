from pydantic import BaseModel, Field
from typing import Optional, Union


class DoctorBase(BaseModel):
    id: Optional[int] = None
    full_name: str
    about: Union[int, str]
    age: int= Field(ge=18)
    specialization: str
    experience: int = Field(ge=1)

    class Config:
        orm_mode = True
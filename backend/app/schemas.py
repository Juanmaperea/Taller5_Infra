from pydantic import BaseModel

class StudentBase(BaseModel):
    name: str
    age: int
    favorite_color: str

class StudentCreate(StudentBase):
    pass

class StudentResponse(StudentBase):
    id: int
    class Config:
        orm_mode = True

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.student_model import Student
from app.schemas import StudentCreate, StudentResponse

router = APIRouter(prefix="/students", tags=["students"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[StudentResponse])
def list_students(db: Session = Depends(get_db)):
    return db.query(Student).all()

@router.post("/", response_model=StudentResponse)
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    new = Student(**student.dict())
    db.add(new)
    db.commit()
    db.refresh(new)
    return new

@router.put("/{student_id}", response_model=StudentResponse)
def update_student(student_id: int, student: StudentCreate, db: Session = Depends(get_db)):
    existing = db.query(Student).filter(Student.id == student_id).first()
    if not existing:
        raise HTTPException(status_code=404, detail="Student not found")
    existing.name = student.name
    existing.age = student.age
    existing.favorite_color = student.favorite_color
    db.commit()
    db.refresh(existing)
    return existing

@router.delete("/{student_id}")
def delete_student(student_id: int, db: Session = Depends(get_db)):
    existing = db.query(Student).filter(Student.id == student_id).first()
    if not existing:
        raise HTTPException(status_code=404, detail="Student not found")
    db.delete(existing)
    db.commit()
    return {"detail": "Student deleted"}

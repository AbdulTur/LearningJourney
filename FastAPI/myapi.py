from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()


students = {
    1: {
        "name": "Abdul",
        "age": 22,
        "year": "year 4"
    }
}

class Student(BaseModel):
    name: str
    age: int
    year: str


class updateStudent(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    year: Optional[str] = None
@app.get("/")

@app.get("/get-student/{student_id}")
def get_student(student_id: int= Path(..., description="The id of student u want to view")):
    return students[student_id]

@app.get("/get-by-name/{student_id}")

def get_student(*,student_id: int, name: Optional[str]=None, test:int):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    return {"Data":"Not found"}



@app.post("/create-student/{student_id}")

def create_students(student_id: int, student: Student):
    if student_id in students:
        return {"Error":"Student Exists"}
    students[student_id]= student
    return students[student_id]


@app.put("/update-student/{student_id}")

def update_student(student_id: int, student: Student):
    if student_id not in student:
        return {"Error": "Student does not exist"}
    
    students[student_id] = student
    return students[student_id]
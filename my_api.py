from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Fake Database
students = []

# Student Model
class Student(BaseModel):

    id: int
    name: str
    course: str
    age: int


# Home API
@app.get("/")
def home():

    return {
        "message": "FastAPI Server Running"
    }


# GET ALL STUDENTS
@app.get("/students")
def get_students():

    return students


# GET SINGLE STUDENT
@app.get("/students/{student_id}")
def get_student(student_id: int):

    for student in students:

        if student["id"] == student_id:

            return student

    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )


# CREATE STUDENT
@app.post("/students")
def create_student(student: Student):

    students.append(student.dict())

    return {
        "message": "Student added",
        "data": student
    }


# UPDATE STUDENT
@app.put("/students/{student_id}")
def update_student(
    student_id: int,
    updated_student: Student
):

    for index, student in enumerate(students):

        if student["id"] == student_id:

            students[index] = updated_student.dict()

            return {
                "message": "Student updated",
                "data": updated_student
            }

    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )


# DELETE STUDENT
@app.delete("/students/{student_id}")
def delete_student(student_id: int):

    for index, student in enumerate(students):

        if student["id"] == student_id:

            students.pop(index)

            return {
                "message": "Student deleted"
            }

    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )

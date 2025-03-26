from fastapi import FastAPI, Path, Query
from typing import Optional
from pydantic import BaseModel

app = FastAPI()


Students = {
    1 : {
        "name" : "Pietro",
        "age" : 18,
        "year" : "freshman"
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



#Gets Information from dictionary PATH
@app.get("/get-student/{student_id}")
def get_student( student_id : int = Path(..., description="Get Student by ID")):
    if student_id in Students:
        return Students[student_id]
    else:
        return {"error": "Student not found"}
    
#Gets information from students by name QUERY
@app.get("/get-by-name")
def get_by_name(name : str):
    for student_id in Students:
        if Students[student_id]["name"] == name:
            return Students[student_id]
    else:
        return {"error": "Student not found"}

#Gets information from student_id and searches name PATH & QUERY 
@app.get("/get-by-name/{student_id}")
def get_by_name(*, student_id : int, name : Optional[str] = None):
    for student_id in Students:
        if Students[student_id]["name"] == name:
            return Students[student_id]
    else:
        return {"error": "Student not found"}



#Post Information inside dictionary with BaseModel
@app.post("/create-student/{student_id}")
def create_student(student_id: int, student: Student):
    if student_id in Students:
        return {"error": "Student already exists"}

    Students[student_id] = student
    return Students[student_id]

#Updates Information from dictionary
@app.put("/update-student/{student_id}")
def update_student(student_id: int, student: updateStudent):
    if student_id not in Students:
        return {"error": "Student not found"}
    if student.name != None:
        Students[student_id].name = student.name
    if student.age != None:
        Students[student_id].age = student.age
    if student.year != None:
        Students[student_id].year = student.year

    return Students[student_id]

"""
#Deletes Information from somewhere
@app.delete("/")
def index():
    return


"""
from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
from models import Model_DB
from Schemas import Course,schedule

from config.base_connection import SessionLocal
from typing import Any,List


course = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
@course.get("/courses/getCourse",response_model=List[Course.data])
def getCourse( db: Session = Depends(get_db) )-> Any:
    resultados = db.query(
        Model_DB.Class
        ).all()

    if not resultados:
        raise HTTPException(status_code=404, detail="error error :C")
    
    response = [Course.data.model_validate(couser) 
                 
                 for couser in resultados 
                  ]
    return response

@course.get("/students/getStudents/{id_curso}", response_model=None)
async def getStudents(id_curso = int ,db: Session = Depends(get_db)) -> Any:
    resultados = db.query(
        Model_DB.Students
        ).join(
            Model_DB.StudentClass,
            Model_DB.StudentClass.id_student == Model_DB.Students.id
        ).join(
            Model_DB.Class,
            Model_DB.Class.id == Model_DB.StudentClass.id_class   
        ).filter(
            Model_DB.Class.id == id_curso 
        ).all()

    if not resultados:
        raise HTTPException(status_code=404, detail="Comentario no encontrado")

    return resultados

@course.get("/courses/getCourses", response_model=List[schedule.data_course])
async def getCourse (db: Session = Depends(get_db)) -> Any:

    resultados = db.query(
        Model_DB.Class,
        Model_DB.Schedule
        ).join(
            Model_DB.Schedule,
            Model_DB.Schedule.id_class == Model_DB.Class.id
        ).all()
        
    if not resultados:
        raise HTTPException(status_code=404, detail="usuario inexistente")
    
    course_dict = {}
    for course, schedule_ in resultados:
        if course.id not in course_dict:
            course_dict[course.id] = {
                "id": course.id,
                "name": course.name,
                "schedule": []
            }
        course_dict[course.id]["schedule"].append(schedule.data_schedule(
            day=schedule_.day,
            init_time=schedule_.init_time,
            end_time=schedule_.end_time
        ))

    response = [schedule.data_course(**course_data) for course_data in course_dict.values()]

    return response

@course.get("/courses/getCourse/{id_course}", response_model=List[schedule.data_course])
async def getCourse(id_course: int, db: Session = Depends(get_db)) -> Any:

    resultados = db.query(
        Model_DB.Class,
        Model_DB.Schedule
        ).join(
            Model_DB.Schedule,
            Model_DB.Schedule.id_class == Model_DB.Class.id
        ).filter(
            Model_DB.Class.id== id_course
        ).all()

    if not resultados:
        raise HTTPException(status_code=404, detail="usuario inexistente")
    
    course_dict = {}
    for course, schedule_ in resultados:
        if course.id not in course_dict:
            course_dict[course.id] = {
                "id": course.id,
                "name": course.name,
                "schedule": []
            }
        course_dict[course.id]["schedule"].append(schedule.data_schedule(
            day=schedule_.day,
            init_time=schedule_.init_time,
            end_time=schedule_.end_time
        ))

    response = [schedule.data_course(**course_data) for course_data in course_dict.values()]

    return response


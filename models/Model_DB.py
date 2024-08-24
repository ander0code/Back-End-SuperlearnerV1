from sqlalchemy import  Column, String, Integer, BigInteger, ForeignKey, Date, TIMESTAMP, Enum, Text
from sqlalchemy.orm import relationship
from config.base_connection import Base

class VolunteerClass(Base):
    __tablename__ = 'volunteer_class'
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    id_class = Column(BigInteger, ForeignKey('class.id'))
    id_volunteer = Column(BigInteger, ForeignKey('volunteers.id'))
    
    class_ = relationship("Class",back_populates="Volunteer_class")
    volunteers = relationship("Volunteer",back_populates="Volunteer_class")

class Class(Base):
    __tablename__ = 'class'
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    category = Column(String(255))
    name = Column(String(255))
    status = Column(Integer, default=1)
    created_at = Column(TIMESTAMP, default='CURRENT_TIMESTAMP')
    updated_at = Column(TIMESTAMP, default='CURRENT_TIMESTAMP', onupdate='CURRENT_TIMESTAMP')

    student_class = relationship("StudentClass",back_populates="class_")
    Volunteer_class = relationship("VolunteerClass",back_populates="class_") 
    Attendance_student = relationship("AttendanceStudent",back_populates="class_")
    
class Parents(Base):
    __tablename__ = 'parents'
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    name = Column(String(255))
    last_name = Column(String(255))
    email = Column(String(255), unique=True)
    phone = Column(String(255), unique=True)
    address = Column(String(255))
    district = Column(String(255))
    city = Column(String(255))
    state_department = Column(String(255))
    country = Column(String(255))
    nationality = Column(String(255))
    document_type = Column(String(255))
    document_id = Column(String(255), unique=True)
    birthdate = Column(Date)
    gender = Column(String(50))
    status = Column(Integer, default=1)
    created_at = Column(TIMESTAMP, default='CURRENT_TIMESTAMP')
    updated_at = Column(TIMESTAMP, default='CURRENT_TIMESTAMP', onupdate='CURRENT_TIMESTAMP')

    students = relationship("Students",back_populates="parents")
    birth_parents = relationship("BirthParent",back_populates="parents")
    
    
class Students(Base):
    __tablename__ = 'students'
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    name = Column(String(255))
    last_name = Column(String(255))
    parent_id = Column(BigInteger, ForeignKey('parents.id'))
    nationality = Column(String(255))
    document_type = Column(String(255))
    document_id = Column(String(255), unique=True)
    birthdate = Column(Date)
    gender = Column(String(50))
    status = Column(Integer, default=1)
    created_at = Column(TIMESTAMP, default='CURRENT_TIMESTAMP')
    updated_at = Column(TIMESTAMP, default='CURRENT_TIMESTAMP', onupdate='CURRENT_TIMESTAMP')

    parents = relationship("Parents",back_populates="students")
    Birth_students = relationship("BirthStudent",back_populates="students")
    student_class = relationship("StudentClass",back_populates="students")
    Attendance_student = relationship("AttendanceStudent",back_populates="students")
    
class Volunteer(Base):
    __tablename__ = 'volunteers'
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    name = Column(String(255))
    last_name = Column(String(255))
    email = Column(String(255), unique=True)
    org_email = Column(String(255), unique=True)
    phone = Column(String(255), unique=True)
    nationality = Column(String(255))
    document_type = Column(String(255))
    document_id = Column(String(255), unique=True)
    birthdate = Column(Date)
    gender = Column(String(50))
    status = Column(Integer, default=1)
    created_at = Column(TIMESTAMP, default='CURRENT_TIMESTAMP')
    updated_at = Column(TIMESTAMP, default='CURRENT_TIMESTAMP', onupdate='CURRENT_TIMESTAMP')

    Attendance_student = relationship("AttendanceStudent",back_populates="volunteers")
    Volunteer_class = relationship("VolunteerClass",back_populates="volunteers")

class AttendanceStudent(Base):
    __tablename__ = 'attendance_student'
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    id_student = Column(BigInteger, ForeignKey('students.id'))
    id_volunteer = Column(BigInteger, ForeignKey('volunteers.id'))
    id_class = Column(BigInteger, ForeignKey('class.id'))
    created_date = Column(TIMESTAMP, default='CURRENT_TIMESTAMP')
    status = Column(Enum('ONTIME', 'LATE', 'JUSTIFIED', 'UNJUSTIFIED'))

    class_ = relationship("Class",back_populates="Attendance_student")
    students = relationship("Students",back_populates="Attendance_student")
    volunteers = relationship("Volunteer",back_populates="Attendance_student")

class BirthParent(Base):
    __tablename__ = 'birth_parents'
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    id_parent = Column(BigInteger, ForeignKey('parents.id'))
    city = Column(String(255))
    state_department = Column(String(255))
    country = Column(String(255))
    
    parents = relationship("Parents",back_populates="birth_parents")
    
    
class BirthStudent(Base):
    __tablename__ = 'birth_students'
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    id_student = Column(BigInteger, ForeignKey('students.id'))
    city = Column(String(255))
    state_department = Column(String(255))
    country = Column(String(255))
    
    students = relationship("Students",back_populates="Birth_students")

class Schedule(Base):
    __tablename__ = 'schedule'
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    id_class = Column(BigInteger, ForeignKey('class.id'))
    day = Column(String(50))
    init_time = Column(String(5))
    end_time = Column(String(5))

class StudentClass(Base):
    __tablename__ = 'student_class'
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    id_class = Column(BigInteger, ForeignKey('class.id'))
    id_student = Column(BigInteger, ForeignKey('students.id'))
    
    class_ = relationship("Class",back_populates="student_class")
    students = relationship("Students",back_populates="student_class")

class Users(Base):
    __tablename__ = 'users'
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    email= Column(String(255), nullable=False, unique=True)
    password= Column(String(255), nullable=False)



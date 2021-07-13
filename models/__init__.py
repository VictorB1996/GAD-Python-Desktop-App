from sqlalchemy import Column, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.mysql import VARCHAR, INTEGER, DOUBLE, DATETIME
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

SQLAlchemyBase = declarative_base()


class CustomBaseModel:
    id = Column(INTEGER, primary_key=True, autoincrement=True)
    created_at = Column(DATETIME, server_default=func.now())
    updated_at = Column(DATETIME, server_default=func.now(), server_onupdate=func.now())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Student(SQLAlchemyBase, CustomBaseModel):
    __tablename__ = "students"
    first_name = Column(VARCHAR(128), nullable=False)
    last_name = Column(VARCHAR(128), nullable=False)
    email = Column(VARCHAR(128), nullable=False, unique=True)
    graded_subjects = relationship("Subject", secondary = "student_grades")
    phone = Column(VARCHAR(10), nullable=True, default=None)

    def __repr__(self):
        return self.email


class Subject(SQLAlchemyBase, CustomBaseModel):
    __tablename__ = "subjects"
    name = Column(VARCHAR(128), nullable=False, unique=True)
    graded_users = relationship(Student, secondary = "student_grades")


class StudentGrade(SQLAlchemyBase, CustomBaseModel):
    __tablename__ = "student_grades"
    student_id = Column(INTEGER, ForeignKey(Student.id))
    student = relationship(Student)
    subject_id = Column(INTEGER, ForeignKey(Subject.id))
    subject = relationship(Subject)
    value = Column(DOUBLE(precision=4, scale=2), nullable=False)

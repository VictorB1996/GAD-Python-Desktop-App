import tkinter
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from gui import Field
from models import Student, Subject, StudentGrade

engine = create_engine("mysql+mysqldb://root:pass@localhost:3306/students_example")
Session = sessionmaker(engine)


def read_from_db():
    pass


def save_grade(firstname, lastname, email, subject_name, grade):
    with Session() as session:
        student = Student(
            first_name=firstname,
            last_name=lastname,
            email=email
        )
        session.add(student)
        session.commit()

        subject = Subject(name=subject_name)
        session.add(subject)
        session.commit()

        student_grade = StudentGrade(
            student=student,
            subject=subject,
            value=grade
        )
        session.add(student_grade)
        session.commit()


if __name__ == "__main__":
    window = tkinter.Tk()
    window.geometry("800x600")
    window.title("Students DB")

    inner_frame = tkinter.Frame(window)
    inner_frame.pack()

    first_name_field = Field(inner_frame, "First Name")
    last_name_field = Field(inner_frame, "Last Name")
    email_field = Field(inner_frame, "E-mail")
    subject_name_field = Field(inner_frame, "Subject Name")
    student_grade_field = Field(inner_frame, "Grade")

    save_button = tkinter.Button(
        inner_frame,
        text="Save Grade",
        command=lambda: save_grade(
            first_name_field.entry.get(),
            last_name_field.entry.get(),
            email_field.entry.get(),
            subject_name_field.entry.get(),
            student_grade_field.entry.get()
        )
    )
    save_button.pack()

    window.mainloop()


# if __name__ == "__main__":
#     with Session() as session:
        # students = session.query(Student).all()

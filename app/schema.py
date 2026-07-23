import strawberry
from strawberry.schema.config import StrawberryConfig


# -----------------------------
# Output Type
# -----------------------------
@strawberry.type
class Student:
    id: int
    name: str
    age: int


# -----------------------------
# Input Type
# -----------------------------
@strawberry.input
class StudentInput:
    id: int
    name: str
    age: int
    department: str
    email: str
    phone: str


# -----------------------------
# Fake Database
# -----------------------------
STUDENTS = [
    Student(id=1, name="Prasanna", age=30),
    Student(id=2, name="John", age=25),
]


# -----------------------------
# Query
# -----------------------------
@strawberry.type
class Query:

    @strawberry.field
    def students(self) -> list[Student]:
        return STUDENTS


# -----------------------------
# Mutation
# -----------------------------
@strawberry.type
class Mutation:

    @strawberry.mutation
    def create_student(
        self,
        student: StudentInput,
    ) -> Student:

        student_data = Student(
            id=student.id,
            name=student.name,
            age=student.age,
        )

        STUDENTS.append(student_data)

        return student_data
       

schema = strawberry.Schema(query=Query, mutation=Mutation, config=StrawberryConfig(auto_camel_case=False))
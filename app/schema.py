import strawberry
from strawberry.schema.config import StrawberryConfig

@strawberry.type
class Student:
    name:str
    id:int 
    age:int
# -----------------------------
# Fake Database
# -----------------------------
STUDENTS = [
    Student(id=1, name="Prasanna", age=30),
    Student(id=2, name="John", age=25),
    Student(id=3, name="Alice", age=21),
]

@strawberry.type
class Query:

    @strawberry.field
    def student(self) -> Student:
        return Student(
            id=1,
            name="Prasanna",
            age=30,
        )

@strawberry.type
class Mutation:

    @strawberry.mutation
    def create_student(self, name:str, age:int)->Student:
        student_4 = Student(
            id = len(STUDENTS)+1,
            name = name,
            age=age
        )
        STUDENTS.append(student_4)
        return student_4

    @strawberry.mutation
    def update_student(
        self,
        id: int,
        name: str,
        age: int,
    ) -> Student:

        for student in STUDENTS:

            if student.id == id:
                student.name = name
                student.age = age

                return student

        raise ValueError(f"Student with id={id} not found")

schema = strawberry.Schema(query=Query, mutation=Mutation, config=StrawberryConfig(auto_camel_case=False))
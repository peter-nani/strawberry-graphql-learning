import strawberry
from strawberry.schema.config import StrawberryConfig

@strawberry.type
class Student:
    id:int
    name:str
    age:int

@strawberry.input
class StudentInput:
    id:int
    name:str
    age:int

STUDENTS = []

@strawberry.type
class Mutation:

    @strawberry.mutation
    def create_student(
        self,
        student:StudentInput,
    )->Student:
        new_student = Student(
            id = student.id,
            age = student.age,
            name = student.name,
        )
        STUDENTS.append(new_student)
        return new_student

@strawberry.type
class Query:

    @strawberry.field
    def students(self) -> list[Student]:
        return STUDENTS




schema = strawberry.Schema(query=Query, mutation=Mutation, config=StrawberryConfig(auto_camel_case=False))
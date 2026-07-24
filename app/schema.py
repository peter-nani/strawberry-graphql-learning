import strawberry
from strawberry.schema.config import StrawberryConfig

@strawberry.type
class Manager:
    id:int
    name:str

@strawberry.type
class Department:
    id:int
    name:str
    location:str
    manager:Manager

@strawberry.type
class Student:
    id:int
    name:str
    age:int
    department:Department

    @strawberry.field
    def Student_info(self)->str:
        return f"{self.name} {self.age} {self.department}"

SURESH = Manager(
    id=1,
    name="Suresh"
)

RAJESH = Manager(
    id=2,
    name="Rajesh"
)

IT = Department(
    id=1,
    name="information tech",
    location="hyderabad",
    manager=SURESH
)

HR = Department(
    id=2,
    name="HR",
    location="Bangalore",
    manager=RAJESH
)

STUDENTS = [

    Student(
        id=1,
        name="Prasanna",
        age=30,
        department=IT,
    ),

    Student(
        id=2,
        name="John",
        age=25,
        department=HR,
    ),

]

@strawberry.input
class StudentInput:
    id:int
    name:str
    age:int

# STUDENTS = []

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
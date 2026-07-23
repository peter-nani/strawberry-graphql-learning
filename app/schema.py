import strawberry


# -----------------------------
# Output Type
# -----------------------------
@strawberry.type
class Student:
    name:str
    age:int
    id:int

STUDENTS = [
     Student(name="prasanna kumar", age=23, id=1),
     Student(name="peter nani", age=23, id=2),
     ]


# -----------------------------
# Query
# -----------------------------
@strawberry.type
class Query:
    @strawberry.field
    def all_students(self)->list[Student]:
            return STUDENTS

schema = strawberry.Schema(Query)

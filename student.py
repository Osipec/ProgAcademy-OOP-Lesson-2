from person import Person

class Student(Person):
    def __init__(self, name: str, surname: str, id: int):
        super().__init__(name, surname)
        self.id = id

    def __str__(self):
        return f'{self.name} {self.surname}, ID: {self.id}'
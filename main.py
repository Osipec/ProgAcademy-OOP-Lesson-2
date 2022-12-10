import logging


class Person:
    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname

    def __str__(self):
        return f'{self.name} {self.surname}'


class Student(Person):
    def __init__(self, name: str, surname: str, id: int):
        super().__init__(name, surname)
        self.id = id

    def __str__(self):
        return f'{self.name} {self.surname}, ID: {self.id}'


class Group():
    def __init__(self, course: str, max_stud):
        self.course = course
        self.max_stud = max_stud
        self.__group = []

    def add_visitor(self, student: Student):
        try:
            if len(self.__group) >= self.max_stud:
                raise MaxStudError("Maximum of students reached", len(self.__group))
        except MaxStudError as err:
            print(err)
        else:
            if student not in self.__group:
                self.__group.append(student)

    def remove_visitor(self, student: Student):
        if student in self.__group:
            self.__group.remove(student)

    def find_visitor(self, surname):
        res = []
        for student in self.__group:
            if student.surname == surname:
                res.append(student)
        return res

    def __str__(self):
        return f'{self.course}: \n' + '\n'.join(map(str, self.__group))


class MaxStudError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value

    def __str__(self):
        return f'MaxStudError: {self.message}, {self.value}'


group = Group('Python', 3)

stud_1 = Student('Kostya', 'Osypenko', 33)
stud_2 = Student('Mykola', 'Slobodyanik', 32)
stud_3 = Student('Liza', 'Bernich', 25)
stud_4 = Student('Serhiy', 'Voevoda', 42)

group.add_visitor(stud_1)
group.add_visitor(stud_2)
group.add_visitor(stud_3)
group.add_visitor(stud_4)

# group.remove_visitor(stud_4)
# group.remove_visitor(stud_3)

print(group)
res = group.find_visitor('Bernich')
for item in res:
    print(f'Search result: {item}')


import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

filehandler = logging.FileHandler(__name__)
filehandler.setLevel(logging.INFO)
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
filehandler.setFormatter(file_formatter)
consolehandler = logging.StreamHandler()
consolehandler.setLevel(logging.WARNING)
cons_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
consolehandler.setFormatter(cons_formatter)

logger.addHandler(filehandler)
logger.addHandler(consolehandler)

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
        """
        This method is called to add student to a group. Student should be an instance of "Student" Class
        Note the exceptions raised in this method
        """
        if not isinstance(student, Student):
            raise TypeError('Student must be instance of class "Student"')
        if len(self.__group) >= self.max_stud:
            raise MaxStudError("Maximum of students reached", len(self.__group))
        if student in self.__group:
            logger.warning(StudInGroupError("Student already in group", student))
            raise StudInGroupError("Student already in group", student)
        self.__group.append(student)
        logger.info('Student added')

    def remove_visitor(self, student: Student):
        """
        This method is used to remove stydent from the group.Student should be an instance of "Student" Class
        """
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
    """
        This exception is raised when you try to add student to a group
        which is already full
    """

    def __init__(self, message, value):
        self.message = message
        self.value = value

    def __str__(self):
        return f'{self.message}, {self.value}'


class StudInGroupError(Exception):
    """
    This exception is raised when you try to add student who is already in group
    """

    def __init__(self, message, student):
        self.message = message
        self.student = student

    def __str__(self):
        return f'{self.message}, {self.student}'

if __name__ == '__main__':

    logger.warning('Started loggin to console and file')
    group = Group('Python', 3)

    stud_1 = Student('Kostya', 'Osypenko', 33)
    stud_2 = Student('Mykola', 'Slobodyanik', 32)
    stud_3 = Student('Liza', 'Bernich', 25)
    stud_4 = Student('Serhiy', 'Voevoda', 42)

    group.add_visitor(stud_1)
    group.add_visitor(stud_2)
    group.add_visitor(stud_3)
    # group.add_visitor(stud_4)

    # group.remove_visitor(stud_4)
    # group.remove_visitor(stud_3)

    print(group)
    res = group.find_visitor('Bernich')
    for item in res:
        print(f'Search result: {item}')

    logger.warning('Logging finished')

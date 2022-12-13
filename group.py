from student import Student
from exceptions import *
from logger import *

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
            logger.warning(MaxStudError("Maximum of students reached", len(self.__group)))
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
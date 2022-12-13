from student import Student
from group import Group
from logger import logger


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

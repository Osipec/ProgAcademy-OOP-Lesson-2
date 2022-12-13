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
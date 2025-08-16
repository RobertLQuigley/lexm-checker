class User:
    def __init__(self, username = None, course = None):
        self.username = username
        self.course = course
        self.section = None

    def __eq__(self, other):
        if type(self) is type(other):
            return self.__dict__ == other.__dict__
        else:
            raise NotImplemented

    def __hash__(self):
        return hash(self.username + self.course)

    def __str__(self):
        return f"Student: {self.username}\nCourse: {self.course}\nSection: {self.section}"

    def assign_section(self, section):
        self.section = section
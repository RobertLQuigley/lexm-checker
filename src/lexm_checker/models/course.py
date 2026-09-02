class Course:
    def __init__(self, course_id, course_name, sections = None):
        self.course_id = course_id
        self.course_name = course_name
        self.sections = []
        for section in sections:
            self.add_section(section)

    def __eq__(self, other):
        if type(self) is type(other):
            return self.__dict__ == other.__dict__
        else:
            raise NotImplemented

    def __hash__(self):

        return hash(self.course_id + self.course_name + ",".join(self.sections))

    def __str__(self):
        return f"Course ID: {self.course_id}\nCourse: {self.course_name}\nSections: {",".join(self.sections)}"


    def add_section(self, section):
        if section in self.sections:
            raise KeyError("Section already exists")
        self.sections.append(section)
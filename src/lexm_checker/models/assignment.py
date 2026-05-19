from lexm_checker.models.rubric import Rubric


class Assignment:
    def __init__(self, name: str, rubric: Rubric | None = None):
        self.name = name
        self.rubric = rubric

    def add_rubric(self, rubric: Rubric):
        self.rubric = rubric
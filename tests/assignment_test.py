from src.lexm_checker.models.assignment import Assignment
from src.lexm_checker.models.rubric import Rubric


class TestAssignment:
    def test_assignment(self):
        assignment = Assignment("Name")
        assert assignment.name == "Name"
        assert assignment.rubric is None

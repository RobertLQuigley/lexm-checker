from src.lexm_checker.models.assignment import Assignment


class TestAssignment:
    def test_assignment(self):
        assignment = Assignment("Name")
        assert assignment.name == "Name"
        assert assignment.rubric == ""

    def test_rubric(self):
        assignment = Assignment("Name")
        assignment.add_rubric("filepath.txt")
        assert assignment.rubric == "filepath.txt"

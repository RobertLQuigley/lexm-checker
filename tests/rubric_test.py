import unittest

from lexm_checker.models.rubric import Rubric

class TestRubric:
    def test_rubric(self):
        rubric = Rubric("test.rubric")
        assert rubric.filename == "test.rubric"
        assert len(rubric.lines) == 0

    def test_quick_compare(self):
        rubric = Rubric("test.rubric")
        empty_lines = []
        good_lines = ["1", "2"]
        assert rubric.quick_compare(empty_lines) == True
        assert rubric.quick_compare(good_lines) == False

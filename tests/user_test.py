from src.lexm_checker.models.user import User

class TestUser:
    def test_init(self):
        default_user = User()
        user = User("test", None)
        full_user = User("test", "course")
        assert default_user.username is None
        assert default_user.course is None
        assert user.username == "test"
        assert user.course is None
        assert full_user.username == "test"
        assert full_user.course == "course"

    def test_comparison(selfs):
        user1 = User("test", "course")
        user2 = User("test", "course")
        user3 = User()

        assert user1 == user2
        assert user1 != user3

    def test_assign_section(self):
        user = User("test", "course")
        user.assign_section("CIS118")
        assert user.section == "CIS118"

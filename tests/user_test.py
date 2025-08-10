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

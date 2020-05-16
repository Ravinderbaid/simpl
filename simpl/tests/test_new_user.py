import mock
from model.user import User
from commands.new.new_user import CmdNewUser
from model.exceptions import InvalidCreditLimitException


class TestNewUser:
    def setup(self):
        self.object_new_user = CmdNewUser()
        self.new_merchant = User("ua", "ma@gmail.com", 1000)

    @mock.patch("model.user.User", return_value=None)
    def test_process(self, mock_object):
        assert self.object_new_user.process(
            "ub", "ub@gmail.com", 10) is None

    @mock.patch("model.user.User", side_effect=InvalidCreditLimitException())
    def test_process_negative_amount(self, mock_exceptions):
        try:
            self.object_new_user.process("uc", "uc@gmail.com", -10)
            assert False
        except KeyError as e:
            assert e.args[0] == "uc"

    def test_process_user_present(self):
        try:
            self.object_new_user.process("ua", "ma@gmail.com", 10)
            assert False
        except Exception as e:
            assert e.args[0] == "User name already exist"

    def test_process_user_str(self):
        try:
            self.object_new_user.process("uaasdasd", "ma@gmail.com", "asdasda")
            assert False
        except Exception:
            assert True

    def test_process_user_key(self):
        try:
            self.object_new_user.process("dasdasdad", "ma@gmail.com", "asdasda")
            assert False
        except Exception:
            assert True

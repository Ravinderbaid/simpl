from commands.payback import CmdPayback
from model.exceptions import (InvalidUserException)
from model.user import User


class TestPayback:

    def setup(self):
        self.object_payback = CmdPayback()

    def test_process(self):
        User.instances["ra"]._remaining_credit = 100
        self.object_payback.process("ra", 10)

    def test_process_user_negative(self):
        try:
            self.object_payback.process("addasdass", 1234)
        except InvalidUserException as e:
            assert e.args[0] == "Invalid users"

    def test_process_amount_negative(self):
        self.object_payback.process("ra", -121234) is None

    def test_process_exception(self):
        try:
            self.object_payback.process("rasdas", "aws")
            assert False
        except Exception:
            assert True

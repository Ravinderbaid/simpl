from commands.update import CmdUpdate
from model.exceptions import InvalidMerchantException


class TestUpdate:

    def setup(self):
        self.object_update = CmdUpdate()

    def test_process(self):
        self.object_update.process("merchant", "ma", 10)

    def test_process_user_negative(self):
        try:
            self.object_update.process("merchant", "addasdass", 10)
        except InvalidMerchantException as e:
            assert e.args[0] == "Invalid merchant"

    def test_process_amount_negative(self):
        self.object_update.process("merchant", "ma", -121234) is None

    def test_process_exception(self):
        try:
            self.object_update.process("merchant", ["as","dasdAS"], 123)
            assert False
        except Exception:
            assert True

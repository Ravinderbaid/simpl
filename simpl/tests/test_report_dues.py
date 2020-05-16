import mock
from commands.report.report_dues import CmdReportDues
from model.exceptions import InvalidUserException


class TestReportTotalDues:
    def setup(self):
        self.report_dues = CmdReportDues()

    def test_process(self):
        try:
            self.report_dues.process("rb")
        except InvalidUserException as e:
            assert e.args[0] == "User not present"

    @mock.patch("model.user.User.user_dues", return_values=100.0)
    def test_process_all(self, mock_user_instance):
        self.report_dues.process("ra") is None

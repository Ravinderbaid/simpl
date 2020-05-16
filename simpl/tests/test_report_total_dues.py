import mock
from commands.report.report_total_dues import CmdReportTotalDues


class TestReportTotalDues:
    def setup(self):
        self.report_total_dues = CmdReportTotalDues()

    @mock.patch("model.user.User.instances", return_values=None)
    def test_process(self, mock_user_instances):
        self.report_total_dues.process() is None

    @mock.patch("model.user.User.user_dues", return_values=100.0)
    def test_process_all(self, mock_user_instance):
        self.report_total_dues.process() is None

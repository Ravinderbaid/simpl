import mock
from model.user import User
from commands.report.report_users_at_credit_limit import CmdReportUsersAtCreditLimit


class TestReportUsersAtCreditLimit:
    def setup(self):
        self.report_users_at_credit_limit = CmdReportUsersAtCreditLimit()

    
    def test_process_all(self):
        user_object = User.instances.get("ra")
        user_object._remaining_credit = 0
        self.report_users_at_credit_limit.process() is None

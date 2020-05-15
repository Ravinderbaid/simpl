from ..cmd import Cmd
from .report_discount import CmdReportDiscount
from .report_dues import CmdReportDues
from .report_total_dues import CmdReportTotalDues
from .report_users_at_credit_limit import CmdReportUsersAtCreditLimit
from dispatcher import Dispatcher

report_dispatcher = Dispatcher()
report_dispatcher.register_command("discount", CmdReportDiscount)
report_dispatcher.register_command("dues", CmdReportDues)
report_dispatcher.register_command("total-dues", CmdReportTotalDues)
report_dispatcher.register_command(
    "users-at-credit-limit", CmdReportUsersAtCreditLimit)


class CmdReport(Cmd):
    def process(self, command, *args):
        try:
            report_dispatcher.dispatch(command, *args)
        except KeyError:
            print("Invalid keywords used with report")
        except Exception as e:
            print(e.args)

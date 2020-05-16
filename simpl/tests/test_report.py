from commands.report.report import CmdReport


class TestReport:

    def setup(self):
        self.object_report = CmdReport()

    def test_process(self):
        assert self.object_report.process("discount", "ma") is None

    def test_process_negative(self):
        try:
            self.object_report.process(
                "addasdass")
        except KeyError as k:
            assert k.args[0] == "Invalid keywords used with report"

    def test_process_exception(self):
        try:
            self.object_report.process("total-dues", {"1": "123"})
            assert False
        except Exception:
            assert True

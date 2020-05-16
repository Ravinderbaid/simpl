from commands.report.report_discount import CmdReportDiscount


class TestReportDiscount:
    def setup(self):
        self.object_discount = CmdReportDiscount()

    def test_process(self):
        assert self.object_discount.process("ma") is None

    def test_process_negative(self):
        try:
            self.object_discount.process("mc")
            assert False
        except Exception as e:
            assert e.args[0] == "Merchant not found"

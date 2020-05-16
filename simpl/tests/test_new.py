from commands.new.new import CmdNew


class TestNew:

    def setup(self):
        self.object_new = CmdNew()

    def test_process(self):
        assert self.object_new.process(
            "user", "rnew", "rnew@gmail.com", 1000) is None

    def test_process_negative(self):
        try:
            self.object_new.process(
                "userasdas", "rnew", "rnew@gmail.com", 1000)
        except KeyError as k:
            assert k.args[0] == "Invalid keywords used with new"

    def test_process_exception(self):
        try:
            self.object_new.process("user", "rnew", {"1": 123})
            assert False
        except Exception:
            assert True

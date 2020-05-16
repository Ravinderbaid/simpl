import mock
from model.merchant import Merchant
from commands.new.new_merchant import CmdNewMerchant
from model.exceptions import InvalidDiscountException


class TestNewMerchant:
    def setup(self):
        self.object_new_merchant = CmdNewMerchant()
        self.new_merchant = Merchant("ma", "ma@gmail.com", 1.25)

    @mock.patch("model.merchant.Merchant", return_value=None)
    def test_process(self, mock_object):
        assert self.object_new_merchant.process(
            "mb", "mb@gmail.com", 10) is None

    @mock.patch("model.merchant.Merchant", side_effect=InvalidDiscountException())
    def test_process_negative_discount(self, mock_exceptions):
        try:
            self.object_new_merchant.process("mc", "mb@gmail.com", -10)
            assert False
        except Exception as e:
            assert e.args[0] == "mc"

    def test_process_merchant_present(self):
        try:
            self.object_new_merchant.process("ma", "ma@gmail.com", 10)
            assert False
        except Exception as e:
            assert e.args[0] == "Merchant name already exist"

    def test_process_merchant_amount_str(self):
        try:
            self.object_new_merchant.process("mzstr", "ma@gmail.com", "10asd")
            assert False
        except Exception:
            assert True

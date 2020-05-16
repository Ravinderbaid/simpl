from model.transaction import Transaction
from model.exceptions import InvalidTransactionAmountException


class TestTransaction:
    def setup(self):
        self.new_transact = Transaction("ravinder", "testmerchant", 100)

    def test_validate_amount(self):
        assert self.new_transact.amount == 100

    def test_validate_amount_negative(self):
        try:
            Transaction("ravinder", "testmerchant", -1000.0)
            assert False
        except InvalidTransactionAmountException as e:
            assert e.args[0] == "Amount should not be greater than 0"

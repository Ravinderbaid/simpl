import mock
from model.merchant import Merchant
from model.user import User
from model.transaction import Transaction
from model.exceptions import InsufficientCreditException, InvalidTransactionAmountException
from commands.new.new_transaction import CmdNewTransaction


class TestNewTransaction:
    def setup(self):
        self.object_new_transaction = CmdNewTransaction()
        self.new_merchant = Transaction("ua", "ma", 100.25)
        User("ra", "ra@gmail.com", 1234)
        Merchant("ama", "ma@gmail.com", 1.234)

    @mock.patch("model.transaction.Transaction", return_value=None)
    @mock.patch("model.user.User.request_credit", return_value=True)
    def test_process(self, mock_object, mock_user):
        assert self.object_new_transaction.process(
            "ra", "ama", 10) is None

    @mock.patch("model.transaction.Transaction", return_value=None)
    @mock.patch("model.user.User.request_credit", side_effect=InsufficientCreditException())
    def test_process_negative_request_credit(self, mock_transcation, mock_exception):
        try:
            self.object_new_transaction.process("ra", "ama", 10213213)
            assert False
        except Exception as e:
            assert e.args[0] == "rejected: reason : Credit Limit"

    @mock.patch("model.transaction.Transaction", side_effect=InvalidTransactionAmountException())
    def test_process_negative_transaction_amount(self, mock_exception):
        try:
            self.object_new_transaction.process("ra", "ama", -10)
            assert False
        except Exception:
            assert True

    def test_process_invalid_user_merchant(self):
        try:
            self.object_new_transaction.process("ub", "masd", -10)
            assert False
        except Exception as e:
            assert e.args[0] == "rejected: reason: Invalid user or merchant"

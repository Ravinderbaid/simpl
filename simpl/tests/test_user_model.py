from model.user import User
from model.exceptions import (
    InsufficientCreditException,
    InvalidPaybackAmountException,
    InvalidCreditLimitException,
)


class TestUser:

    def setup(self):
        self.test_user = User("test", "test@simpl.com", 1000)

    def test_user_set_credit_limit(self):
        new_user = User("ravinder", "ravinder@simpl.com", 1000)
        assert new_user.credit_limit == 1000

    def test_user_set_credit_limit_negative(self):
        try:
            User("ravinder", "ravinder@simpl.com", -1000)
            assert False
        except InvalidCreditLimitException as e:
            assert e.args[0] == "Credit limit cannot be less than 0"

    def test_user_credit_request(self):
        assert self.test_user.request_credit(1000)

    def test_user_credit_request_negative(self):
        try:
            self.test_user.request_credit(1001)
            assert False
        except InsufficientCreditException as e:
            assert e.args[
                0] == f"Amount 1001 exceeds the remaining credit limit: {self.test_user._remaining_credit}"

    def test_user_payback(self):
        self.test_user._remaining_credit = 200
        assert self.test_user.payback(100) is None

    def test_user_payback_negative(self):
        try:
            self.test_user.payback(10001)
            assert False
        except InvalidPaybackAmountException as e:
            assert e.args[0] == "Trying to pay back more than needed"

    def test_user_dues(self):
        assert self.test_user.user_dues() == self.test_user.credit_limit - \
            self.test_user._remaining_credit

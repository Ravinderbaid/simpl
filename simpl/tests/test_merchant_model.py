from model.merchant import Merchant
from model.exceptions import InvalidDiscountException


class TestMerchant:

    def setup(self):
        self.test_merchant = Merchant("testmerchant", "test@simpl.com", 10)

    def test_user_set_dsicount(self):
        assert self.test_merchant.discount == 10

    def test_user_set_dsicount_negative(self):
        try:
            Merchant("testfalse", "test@simpl.com", -10)
            assert False
        except InvalidDiscountException as e:
            assert e.args[0] == "Invalid discount, discount must be greater than 0"

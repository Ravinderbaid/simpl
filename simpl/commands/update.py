from .cmd import Cmd
from model import Merchant, InvalidDiscountException, InvalidMerchantException


class CmdUpdate(Cmd):
    def process(self, type: str,merchant: str, discount: float) -> None:
        try:
            merchant_object = Merchant.instances.get(merchant)
            if merchant_object:
                old_dicount = merchant_object.discount
                merchant_object.discount = discount
                print(f"Discount updated from {old_dicount} to {discount}")
            else:
                raise InvalidMerchantException("Invalid user")
        except InvalidDiscountException as e:
            print(e.args)
        except InvalidMerchantException as e:
            print(e.args)
        except Exception as e:
            print(e.args)

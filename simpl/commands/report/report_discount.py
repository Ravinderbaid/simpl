from ..cmd import Cmd
from model.merchant import Merchant
from model.transaction import Transaction


class CmdReportDiscount(Cmd):
    def process(self, merchant_name: str) -> None:
        merchant_object = Merchant.instances.get(merchant_name)
        merchant_discount = merchant_object.discount
        if merchant_discount:
            transaction_objects = Transaction.instances
            total = 0
            for transaction in transaction_objects:
                transaction_object = transaction_objects[transaction]
                if transaction_object._merchant == merchant_name and transaction_object._status:
                    total += (transaction_object._amount * merchant_discount)/100
            print(total)
        else:
            raise Exception("Merchant not found")

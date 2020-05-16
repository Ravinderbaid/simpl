from ..cmd import Cmd
from model.merchant import Merchant
from model.user import User
from model.transaction import Transaction, TransactionStatus
from model.exceptions import InsufficientCreditException, InvalidTransactionAmountException


class CmdNewTransaction(Cmd):
    def process(self, user: str, merchant: str, amount: float) -> None:
        user_object = User.instances.get(user)
        merchant_object = Merchant.instances.get(merchant)
        if user_object and merchant_object:
            try:
                amount = float(amount)
                Transaction(user, merchant, amount)
                if user_object.request_credit(amount):
                    print("success")
                Transaction.instances[Transaction.transact_count]._status = TransactionStatus.COMPLETED
            except InsufficientCreditException:
                raise Exception("rejected: reason : Credit Limit")
            except InvalidTransactionAmountException:
                raise
            except Exception:
                del Transaction.instances[Transaction.transact_count]
                Transaction.transact_count -= 1
                raise
        else:
            raise Exception("rejected: reason: Invalid user or merchant")

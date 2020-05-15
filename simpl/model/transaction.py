from __future__ import annotations

from enum import IntEnum
from typing import ClassVar, Dict

from .merchant import Merchant
from .user import User
from .exceptions import InvalidTransactionAmountException

__all__ = ["Transaction"]


class TransactionStatus(IntEnum):
    PENDING = 0
    COMPLETED = 1


class Transaction:
    instances: ClassVar[Dict[str, Transaction]]
    _user: User
    _merchant: Merchant
    _amount: float
    _status: TransactionStatus

    transact_count = 0
    instances = {}

    def __init__(self, user_name: str, merchant_name: str, amount: float) -> None:
        self._user = user_name
        self._merchant = merchant_name
        self.amount = float(amount)
        self._status = TransactionStatus.PENDING
        Transaction.transact_count += 1
        Transaction.instances[Transaction.transact_count] = self

    @property
    def amount(self) -> float:
        return self._amount

    @amount.setter
    def amount(self, value) -> None:
        if value <= 0:
            raise InvalidTransactionAmountException(
                "Amount should not be greater than 0"
            )
        self._amount = value

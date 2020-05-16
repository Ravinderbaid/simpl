from __future__ import annotations

from typing import ClassVar, Dict

from .customer import Customer
from .exceptions import (
    InsufficientCreditException,
    InvalidPaybackAmountException,
    InvalidCreditLimitException,
)

__all__ = ["User"]


class User(Customer):
    instances: ClassVar[Dict[str, User]]
    _credit_limit: float
    _remaining_credit: float

    instances = {}

    def __init__(self, name: str, email: str, limit: float) -> None:
        super().__init__(name=name, email=email)
        User.instances[name] = self
        self.credit_limit = float(limit)
        self._remaining_credit = float(limit)

    @property
    def credit_limit(self) -> float:
        return self._credit_limit

    @credit_limit.setter
    def credit_limit(self, value) -> None:
        if value < 0:
            raise InvalidCreditLimitException(
                "Credit limit cannot be less than 0")
        self._credit_limit = float(value)

    def request_credit(self, amount: float) -> None:
        if self._remaining_credit < amount:
            raise InsufficientCreditException(
                f"Amount {amount} exceeds the remaining credit limit: {self._remaining_credit}"
            )
        self._remaining_credit -= amount
        return True

    def payback(self, amount: float) -> None:
        maximum_payable = self._credit_limit - self._remaining_credit
        if amount > maximum_payable:
            raise InvalidPaybackAmountException(
                "Trying to pay back more than needed"
            )
        self._remaining_credit += amount

    def user_dues(self) -> float:
        return self.credit_limit - self._remaining_credit

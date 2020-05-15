from __future__ import annotations

from typing import ClassVar, Dict

from .customer import Customer
from .exceptions import InvalidDiscountException

__all__ = ["Merchant"]


class Merchant(Customer):
    instances: ClassVar[Dict[str, Merchant]]
    _discount: float

    instances = {}

    def __init__(self, name: str, email: str, discount: float) -> None:
        Merchant.instances[name] = self
        super().__init__(name=name, email=email)
        self.discount = float(discount)

    @property
    def discount(self) -> float:
        return self._discount

    @discount.setter
    def discount(self, value: float) -> None:
        if value <= 0:
            raise InvalidDiscountException(
                "Invalid discount, discount must be greater than 0"
            )
        self._discount = value

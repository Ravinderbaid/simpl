from __future__ import annotations

import re

from .exceptions import EmailException, NameException

__all__ = ["Customer"]


class Customer:
    _name: str
    _email: str

    def __init__(self, name: str, email: str) -> None:
        self.name = name
        self.email = email

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        if not re.match(r"[a-zA-Z]+$", value):
            raise NameException(
                "Name format invalid: name may only consist of letter")
        self._name = value

    @property
    def email(self) -> str:
        return self._email

    @email.setter
    def email(self, value: str) -> None:
        if not re.match(r"^[a-zA-Z]{2,}@[a-zA-Z]{3,}.[a-z]{2,3}$", value):
            raise EmailException(
                "Email format invalid. Expected: [<more_than_two_letter>@<more_than_three_letter>.<not_more_than_two_to_three_letter>]+(*All in small case)"
            )
        self._email = value

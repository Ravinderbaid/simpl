from .cmd import Cmd
from model.user import User
from model.exceptions import (InvalidUserException,
                              InvalidPaybackAmountException)


class CmdPayback(Cmd):
    def process(self, user: str, amount: float) -> None:
        try:
            amount = float(amount)
            if amount < 0:
                raise InvalidPaybackAmountException(
                    "Amount should be greater than 0")
            user_object = User.instances.get(user)
            if user_object:
                user_object.payback(amount)
                print(f"{user}(dues: {user_object.user_dues()})")
            else:
                raise InvalidUserException("Invalid user")
        except InvalidPaybackAmountException as e:
            print(e.args)
        except InvalidUserException as e:
            print(e.args)
        except Exception as e:
            print(e.args)

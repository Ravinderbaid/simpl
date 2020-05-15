from ..cmd import Cmd
from model.user import User
from model.exceptions import InvalidUserException


class CmdReportDues(Cmd):
    def process(self, user_name: str) -> None:
        user_object = User.instances.get(user_name)
        if user_object:
            print(user_object.user_dues())
        else:
            raise InvalidUserException("User not present")

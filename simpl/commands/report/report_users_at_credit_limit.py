from ..cmd import Cmd
from model.user import User


class CmdReportUsersAtCreditLimit(Cmd):
    def process(self) -> None:
        user_objects = User.instances
        for user_name in user_objects:
            user_object = user_objects[user_name]
            dues = user_object.user_dues()
            if dues == user_object.credit_limit:
                print(user_name)

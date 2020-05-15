from ..cmd import Cmd
from model.user import User


class CmdReportTotalDues(Cmd):
    def process(self) -> None:
        user_objects = User.instances
        total = 0
        for user_name in user_objects:
            user_object = user_objects[user_name]
            dues = user_object.user_dues()
            if dues:
                print(f"{user_name} : {dues}")
                total += dues
        print(f"total: {total}")

from ..cmd import Cmd
from model.user import User


class CmdNewUser(Cmd):
    def process(self, name: str, email: str, limit: float) -> None:
        if not User.instances.get(name):
            try:
                User(name, email, limit)
                print(f"{name}({limit})")
            except KeyError as k:
                raise Exception(k.args)
            except Exception:
                del User.instances[name]
                raise
        else:
            raise Exception("User name already exist")

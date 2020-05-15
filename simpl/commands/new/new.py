from ..cmd import Cmd
from .new_merchant import CmdNewMerchant
from .new_user import CmdNewUser
from .new_transaction import CmdNewTransaction
from dispatcher import Dispatcher

new_dispatcher = Dispatcher()
new_dispatcher.register_command("user", CmdNewUser)
new_dispatcher.register_command("merchant", CmdNewMerchant)
new_dispatcher.register_command("txn", CmdNewTransaction)


class CmdNew(Cmd):
    def process(self, command, *args):
        try:
            new_dispatcher.dispatch(command, *args)
        except KeyError:
            print("Invalid keywords used with new")
        except Exception as e:
            print(e.args)

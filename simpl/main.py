from commands import CmdNew, CmdPayback, CmdReport, CmdUpdate
from dispatcher import Dispatcher

main_dispatcher = Dispatcher()
main_dispatcher.register_command("new", CmdNew)
main_dispatcher.register_command("report", CmdReport)
main_dispatcher.register_command("payback", CmdPayback)
main_dispatcher.register_command("update", CmdUpdate)


def main():
    while True:
        inp = input("").strip().lower()
        if not inp:
            break
        command, *args = inp.split()
        main_dispatcher.dispatch(command, *args)


if __name__ == "__main__":
    main()

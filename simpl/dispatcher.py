from typing import Dict, Type

from commands import Cmd


class Dispatcher:
    _commands: Dict[str, Type[Cmd]]

    def __init__(self):
        self._commands = {}

    def register_command(self, command, handler: Type[Cmd]) -> None:
        self._commands[command] = handler

    def dispatch(self, command, *args) -> None:
        handler = self._commands[command]
        handler().process(*args)

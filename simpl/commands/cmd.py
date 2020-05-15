from abc import ABC, abstractmethod

__all__ = ["Cmd"]


class Cmd(ABC):
    @abstractmethod
    def process(self, *args: str) -> None:
        pass

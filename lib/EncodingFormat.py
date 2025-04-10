from abc import ABC, abstractmethod


class EncodingFormat(ABC):
    """Abstract Base class for an encoding format"""

    @abstractmethod
    def encode(self, data: str | int) -> str:
        pass

    @abstractmethod
    def decode(self, data: str | int) -> str:
        pass

    @abstractmethod
    def info(self) -> str:
        pass

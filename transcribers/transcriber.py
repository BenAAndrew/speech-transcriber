from abc import ABC, abstractmethod

class Transcriber(ABC):
    @abstractmethod
    def transcribe(self, path: str) -> str:
        """ Transcribes a given audio file path. """
        pass

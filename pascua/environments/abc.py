from abc import ABC, abstractmethod

from ..types import Context, SourceCode


class Environment(ABC):

    @abstractmethod
    def up(self):
        pass

    @abstractmethod
    def exec(self, source_code: SourceCode, context: Context) -> Context:
        pass

    @abstractmethod
    def down(self):
        pass

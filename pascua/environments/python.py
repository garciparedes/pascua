from .abc import Environment

from ..types import (
    Dependencies,
    Version,
)


class PythonEnvironment(Environment):

    def __init__(self, version: Version, dependencies: Dependencies = tuple()):
        self.version = version
        self.dependencies = dependencies

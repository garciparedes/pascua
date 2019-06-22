from abc import ABC, abstractmethod
from io import BytesIO
from typing import Sequence
from uuid import uuid4

import docker

from ..types import Context, SourceCode


class Environment(ABC):

    def __init__(self, *args, **kwargs):
        self.uuid = str(uuid4())
        self.container = None
        self.client = docker.from_env()

    @property
    @abstractmethod
    def docker_file(self) -> Sequence[str]:
        pass

    def build(self):
        output = BytesIO('\n'.join(self.docker_file).encode())
        self.client.images.build(fileobj=output, tag=self.uuid)

    def up(self):
        self.build()
        self.container = self.client.containers.run(self.uuid, 'tail -f /dev/null', detach=True)

    def exec(self, source_code: SourceCode, context: Context) -> Context:
        if self.container is None:
            self.up()
        return self._exec(source_code, context)

    @abstractmethod
    def _exec(self, source_code: SourceCode, context: Context) -> Context:
        pass

    def down(self):
        if self.container is not None:
            self.container.stop()

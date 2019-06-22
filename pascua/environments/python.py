import ast
import logging
from typing import Sequence

from .abc import Environment

from ..types import (
    Dependencies,
    Version,
    Context,
    SourceCode,
)
import dill

logger = logging.getLogger(__name__)


class PythonEnvironment(Environment):

    def __init__(self, version: Version, pip_dependencies: Dependencies = None,
                 apt_dependencies: Dependencies = tuple(), *args, **kwargs):
        super().__init__(*args, **kwargs)

        if pip_dependencies is None:
            pip_dependencies = list()

        pip_dependencies.append("dill>=0.29")

        self.version = version
        self.pip_dependencies = pip_dependencies
        self.apt_dependencies = apt_dependencies

    @property
    def raw_apt_dependencies(self):
        return ' '.join(self.apt_dependencies)

    @property
    def raw_pip_dependencies(self):
        return ' '.join(self.pip_dependencies)

    @property
    def docker_file(self) -> Sequence[str]:
        docker_file = [
            f'FROM python:{self.version}',
            f'RUN apt-get update && apt-get install -y {self.raw_apt_dependencies}',
            f'RUN pip install {self.raw_pip_dependencies}',
        ]
        logger.debug(f"Dockerfile: {docker_file}")
        return docker_file

    def _exec(self, source_code: SourceCode, context: Context) -> Context:
        if not isinstance(source_code, str):
            source_code = ';'.join(source_code)

        logger.debug(f"Context: {context}")
        logger.debug(f"Source Code: {source_code}")

        context = dill.dumps(context)
        source_code = dill.dumps(source_code)

        python_sentence = ';'.join([
            f'import dill',
            f'context = dill.loads({context})',
            f'source_code = dill.loads({source_code})',
            f'exec(source_code, context)',
            f'context.pop("__builtins__", None)',
            f'context = dill.dumps(context)',
            f'print(context)',
        ]).replace('"', '\\"')
        logging.debug("Python Sentence: f{python_sentence}")

        python_command = f'python -c "{python_sentence}"'
        logging.debug(f"Python command: {python_command}")

        result = self.container.exec_run(python_command)
        logger.debug(f"Result: {result.output.decode()}")
        context = ast.literal_eval(result.output.decode())
        context = dill.loads(context)
        return context

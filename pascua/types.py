from typing import Any, Dict, Union, Sequence, MutableSequence

Dependency = str
Dependencies = MutableSequence[Dependency]

Version = Union[str, Sequence[str]]

SourceCode = Union[str, Sequence[str]]
Context = Dict[str, Any]

from typing import Any
from pydantic import BaseModel
import pydash

from app.engine.nodes.base import BaseNode, ExecutionResult


class SetNodeConfig(BaseModel):
    path: str
    value: Any


class SetNode(BaseNode[SetNodeConfig]):
    def execute(self, data: dict) -> ExecutionResult:
        result = pydash.set_(data, self._config.path, self._config.value)
        next_nodes = {edge.target for edge in self._edges}

        return ExecutionResult(data=result, next_nodes=next_nodes)

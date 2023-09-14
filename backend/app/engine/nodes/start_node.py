from pydantic import BaseModel, Field
import pydash
from app.engine.nodes.base import BaseNode, ExecutionResult
from app.models.flow import Edge


class StartNodeConfig(BaseModel):
    input_path: str = Field(default="", alias="inputPath")


class StartNode(BaseNode[StartNodeConfig]):
    def execute(self, data: dict) -> ExecutionResult:
        result = pydash.get(data, self._config.input_path, None)
        if result is None:
            raise Exception(f"The input_path '{self._config.input_path}' results None.")

        next_nodes = {edge.target for edge in self._edges}

        return ExecutionResult(data=result, next_nodes=next_nodes)

import pydash
from app.engine.configs.set_node_config import SetNodeConfig

from app.engine.executors.base_executor import NodeExecutor, ExecutionResult


class SetNodeExecutor(NodeExecutor[SetNodeConfig]):
    def execute(self, data: dict) -> ExecutionResult:
        if self._config.path == "":
            result = self._config.value
        else:
            result = pydash.set_(data, self._config.path, self._config.value)
        next_nodes = {edge.target for edge in self._edges}

        return ExecutionResult(data=result, next_nodes=next_nodes)

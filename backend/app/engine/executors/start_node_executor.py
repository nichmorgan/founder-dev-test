import pydash
from app.engine.configs.start_node_config import StartNodeConfig
from app.engine.executors.base_executor import NodeExecutor, ExecutionResult


class StartNodeExecutor(NodeExecutor[StartNodeConfig]):
    def execute(self, data: dict) -> ExecutionResult:
        result = pydash.get(data, self._config.input_path, None)
        if result is None:
            raise Exception(f"The input_path '{self._config.input_path}' results None.")

        next_nodes = {edge.target for edge in self._edges}

        return ExecutionResult(data=result, next_nodes=next_nodes)

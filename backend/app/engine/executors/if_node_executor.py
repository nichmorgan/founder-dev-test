import pydash
from app.engine.configs.if_node_config import IfNodeConfig, IfOperator
from app.engine.executors.base_executor import NodeExecutor, ExecutionResult, NodeConfig
from enum import Enum


class TargetHandle(str, Enum):
    no = "no"
    yes = "yes"


class IfNodeExecutor(NodeExecutor[IfNodeConfig]):
    _operator_map = {
        IfOperator.eq: lambda field, value: field == value,
        IfOperator.lt: lambda field, value: field < value,
        IfOperator.lte: lambda field, value: field <= value,
        IfOperator.gt: lambda field, value: field > value,
        IfOperator.gte: lambda field, value: field >= value,
    }

    _source_handle = {True: TargetHandle.yes, False: TargetHandle.no}

    def __init__(self, params: NodeConfig[IfNodeConfig]) -> None:
        super().__init__(params)
        self._validate_edges()

    def _validate_edges(self) -> None:
        for edge in self._edges:
            if (edge.source_handle or "").lower() not in self._source_handle.values():
                raise ValueError("All edges must has an valid source_handle")

    def execute(self, data: dict) -> ExecutionResult:
        if not pydash.has(data, self._config.path):
            raise ValueError(f"Path '{self._config.path}' not found in payload")

        field_value = pydash.get(data, self._config.path)
        value = self._config.value
        result: bool = self._operator_map[self._config.operator](field_value, value)

        next_nodes = {
            edge.target
            for edge in self._edges
            if pydash.get(edge, "source_handle").lower()
            == self._source_handle[result].lower()
        }

        return ExecutionResult(data=data, next_nodes=next_nodes)

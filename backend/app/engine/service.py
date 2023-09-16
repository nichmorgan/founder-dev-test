import copy
from typing import Any, Generic, Type

from pydantic import BaseModel
from app.engine.executors.base_executor import NodeExecutor, NodeConfig, TConfig
from app.engine.executors.if_node_executor import IfNodeExecutor, IfNodeConfig
from app.engine.executors.set_node_executor import SetNodeExecutor, SetNodeConfig
from app.engine.executors.start_node_executor import StartNodeExecutor, StartNodeConfig
from app.models.flow import Edge, Flow, NodeTypes


class EngineNode(BaseModel, Generic[TConfig]):
    executor_factory: Type[NodeExecutor]
    config_factory: Type[TConfig]


class EngineService:
    _node_factories: dict[NodeTypes, EngineNode] = {
        NodeTypes.START: EngineNode(
            executor_factory=StartNodeExecutor, config_factory=StartNodeConfig
        ),
        NodeTypes.IF: EngineNode(
            executor_factory=IfNodeExecutor, config_factory=IfNodeConfig
        ),
        NodeTypes.SET: EngineNode(
            executor_factory=SetNodeExecutor, config_factory=SetNodeConfig
        ),
    }

    def __init__(self, flow: Flow) -> None:
        self._flow = flow

        self._nodes = {node.id: node for node in flow.nodes}
        self._edges = flow.edges

    def _parse_config(
        self,
        node_type: NodeTypes,
        config: TConfig,
    ) -> TConfig:
        return self._node_factories[node_type].config_factory(**config)

    def _parse_executor(
        self,
        node_type: NodeTypes,
        node_edges: list[Edge],
        config: TConfig,
    ) -> NodeExecutor[TConfig]:
        node_config = NodeConfig(config=config, edges=node_edges)
        return self._node_factories[node_type].executor_factory(node_config)

    def execute(self, data: dict) -> Any:
        if len(self._flow.nodes) == 0:
            return data

        execution_data = copy.deepcopy(data)
        node = self._flow.nodes[0]

        while True:
            if node.type not in self._node_factories:
                raise Exception(f"Unknown node type '{node.type}'.")

            node_edges = [edge for edge in self._edges if edge.source == node.id]
            node_config = self._parse_config(node.type, node.data)
            node_executor = self._parse_executor(node.type, node_edges, node_config)

            execution_result = node_executor.execute(execution_data)
            execution_data = execution_result.data

            if len(execution_result.next_nodes) == 0:
                break

            node = self._flow.get_node_by_id(list(execution_result.next_nodes)[0])

        return execution_data

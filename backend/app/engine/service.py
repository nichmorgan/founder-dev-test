import copy
from app.engine.nodes.start_node import StartNode
from app.models.flow import Flow, NodeTypes


# class EngineService:
#     def __init__(self, flow: Flow) -> None:
#         self._flow = flow

#         self._nodes = {node.id: node for node in flow.nodes}
#         self._edges = self._edges

#     def execute(self, data: dict) -> dict:
#         result = copy.deepcopy(data)

#         for node in self._flow.nodes:
#             if node.type == NodeTypes.START:
#                 node = StartNode(node.data)
#             else:
#                 raise Exception(f"Unknown node type '{node.type}'.")

#             result = node.execute(result)

#         return result

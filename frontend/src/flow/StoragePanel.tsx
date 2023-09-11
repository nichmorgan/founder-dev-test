import { Panel, ReactFlowJsonObject } from "reactflow";
import useBoundStore, { StorageState } from "./lib/storage";

import "./StoragePanel.css";

const FLOW_KEY = "example-flow";

const selector = (state: StorageState) => ({
  nodes: state.nodes,
  edges: state.edges,
  flowInstance: state.flowInstance,
  setFlowInstance: state.setFlowInstance,
  setNodes: state.setNodes,
  setEdges: state.setEdges,
  updateNodeData: state.updateNodeData,
  appendNodes: state.appendNodes,
  onNodesChange: state.onNodesChange,
  onEdgesChange: state.onEdgesChange,
  onConnect: state.onConnect,
});

export default function StoragePanel() {
  const { flowInstance, setNodes, setEdges } = useBoundStore(selector);

  const onSave = () => {
    const flow = flowInstance?.toObject();
    if (flow) localStorage.setItem(FLOW_KEY, JSON.stringify(flow));
  };

  const onRestore = () => {
    if (!flowInstance) return;

    const flowObject = localStorage.getItem(FLOW_KEY);
    if (!flowObject) return;

    const flow: ReactFlowJsonObject = JSON.parse(flowObject);
    const { x = 0, y = 0, zoom = 1 } = flow.viewport;

    setNodes(flow.nodes);
    setEdges(flow.edges);
    flowInstance.setNodes(flow.nodes);
    flowInstance.setEdges(flow.edges);
    flowInstance.setViewport({ x, y, zoom });
  };

  return (
    <Panel position="top-right">
      <button onClick={onSave}>save</button>
      <button onClick={onRestore}>restore</button>
    </Panel>
  );
}

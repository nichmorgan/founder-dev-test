import { useState, useRef, useCallback, useMemo } from "react";
import ReactFlow, {
  ReactFlowProvider,
  Controls,
  ReactFlowInstance,
  Node,
} from "reactflow";

import "reactflow/dist/style.css";

import useBoundStore, { StorageState } from "./lib/storage";
import Sidebar from "./Sidebar";
import StartNode from "./nodes/StartNode";

import "./Flow.css";
import NodeTypes from "./lib/node.types";
import generateNodeId from "./lib/helpers/generate.node.id";
import IfNode from "./nodes/IfNode";
import SetNode from "./nodes/SetNode";

const selector = (state: StorageState) => ({
  nodes: state.nodes,
  edges: state.edges,
  updateNodeData: state.updateNodeData,
  appendNodes: state.appendNodes,
  onNodesChange: state.onNodesChange,
  onEdgesChange: state.onEdgesChange,
  onConnect: state.onConnect,
});

const Flow = () => {
  const reactFlowWrapper = useRef<HTMLInputElement>(null);
  const { nodes, edges, appendNodes, onNodesChange, onEdgesChange, onConnect } =
    useBoundStore(selector);

  const [reactFlowInstance, setReactFlowInstance] =
    useState<ReactFlowInstance | null>(null);

  const nodeTypes = useMemo(
    () => ({
      [NodeTypes.StartNode]: StartNode,
      [NodeTypes.IfNode]: IfNode,
      [NodeTypes.SetNode]: SetNode,
    }),
    []
  );

  const onDragOver = useCallback((event: React.DragEvent) => {
    event.preventDefault();
    event.dataTransfer.dropEffect = "move";
  }, []);

  const onDrop = useCallback(
    (event: React.DragEvent) => {
      event.preventDefault();

      const type = event.dataTransfer.getData("application/reactflow");

      // check if the dropped element is valid
      if (typeof type === "undefined" || !type) return;
      if (reactFlowWrapper.current === null) return;
      if (reactFlowInstance === null) return;

      const reactFlowBounds = reactFlowWrapper.current.getBoundingClientRect();

      const position = reactFlowInstance.project({
        x: event.clientX - reactFlowBounds.left,
        y: event.clientY - reactFlowBounds.top,
      });

      const newNode: Node = {
        id: generateNodeId(),
        type,
        position,
        data: {},
      };

      appendNodes([newNode]);
    },
    [reactFlowInstance]
  );

  return (
    <div className="flow">
      <ReactFlowProvider>
        <div className="reactflow-wrapper" ref={reactFlowWrapper}>
          <ReactFlow
            nodes={nodes}
            edges={edges}
            onNodesChange={onNodesChange}
            onEdgesChange={onEdgesChange}
            onConnect={onConnect}
            onInit={setReactFlowInstance}
            onDrop={onDrop}
            onDragOver={onDragOver}
            nodeTypes={nodeTypes}
            fitView
          >
            <Controls />
          </ReactFlow>
        </div>
        <Sidebar />
      </ReactFlowProvider>
    </div>
  );
};

export default Flow;

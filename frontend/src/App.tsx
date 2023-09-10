import { useState, useRef, useCallback, useMemo } from "react";
import ReactFlow, {
  ReactFlowProvider,
  addEdge,
  useNodesState,
  useEdgesState,
  Controls,
  Connection,
  Edge,
  ReactFlowInstance,
  Node,
  XYPosition,
  applyNodeChanges,
  NodeChange,
} from "reactflow";
import "reactflow/dist/style.css";

import Sidebar from "./Sidebar";
import StartNode, { StartNodeData } from "./StartNode";

import "./Flow.css";
import "./App.css";
import NodeTypes from "./lib/NodeTypes";
import generateNodeId from "./lib/helpers/generate.node.id";

const initialNodes: Node[] = [
  {
    id: "1",
    type: NodeTypes.StartNode,
    data: { inputPath: "" },
    position: { x: 150, y: 0 },
  } as Node<StartNodeData>,
];

const Flow = () => {
  const reactFlowWrapper = useRef<HTMLInputElement>(null);
  const [nodes, setNodes, onNodesChange] = useNodesState(initialNodes);
  const [edges, setEdges, onEdgesChange] = useEdgesState([]);
  const [reactFlowInstance, setReactFlowInstance] =
    useState<ReactFlowInstance | null>(null);

  const nodeTypes = useMemo(() => ({ [NodeTypes.StartNode]: StartNode }), []);

  const onConnect = useCallback(
    (connection: Connection) => setEdges((eds) => addEdge(connection, eds)),
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
        data: undefined,
      };

      setNodes((nds) => nds.concat(newNode));
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

import React from "react";
import NodeTypes from "./lib/node.types";

export default () => {
  const onDragStart = (
    event: React.DragEvent<HTMLDivElement>,
    nodeType: string
  ) => {
    event.dataTransfer.setData("application/reactflow", nodeType);
    event.dataTransfer.effectAllowed = "move";
  };

  return (
    <aside>
      <div className="description">
        You can drag these nodes to the pane on the right.
      </div>
      <div
        className="node start-node"
        onDragStart={(event) => onDragStart(event, NodeTypes.StartNode)}
        draggable
      >
        Start Node
      </div>
      <div
        className="node if-node"
        onDragStart={(event) => onDragStart(event, NodeTypes.IfNode)}
        draggable
      >
        If Node
      </div>
      <div
        className="node set"
        onDragStart={(event) => onDragStart(event, NodeTypes.SetNode)}
        draggable
      >
        Set Node
      </div>
    </aside>
  );
};

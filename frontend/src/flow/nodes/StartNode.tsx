import { useCallback, useState } from "react";
import { Handle, Position } from "reactflow";

// import "./StartNode.css";

export interface StartNodeData {
  inputPath: string;
}

export default function StartNode() {
  const [_path, setPath] = useState("");

  const onChange = useCallback<React.ChangeEventHandler<HTMLInputElement>>(
    (event) => {
      event.preventDefault();
      setPath(event.target.value);
    },
    []
  );

  return (
    <div className="node start-node">
      <div>
        <label htmlFor="inputPath">Input Path ($.):</label>
        <input id="inputPath" name="inputPath" onChange={onChange} />
      </div>
      <Handle type="source" position={Position.Bottom} isConnectable={true} />
    </div>
  );
}

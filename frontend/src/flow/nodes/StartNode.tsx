import { Handle, NodeProps, Position } from "reactflow";
import useBoundStore from "../lib/storage";

import "./StartNode.css";

export interface StartNodeData {
  inputPath: string;
}

export default function StartNode({ id, data }: NodeProps<StartNodeData>) {
  const updateInputPath = useBoundStore(
    (state) => state.updateNodeData<StartNodeData>
  );

  return (
    <div className="node start-node">
      <div>
        <label htmlFor="inputPath">Input Path ($.):</label>
        <input
          id="inputPath"
          name="inputPath"
          defaultValue={data.inputPath}
          onChange={(evt) =>
            updateInputPath(id, { inputPath: evt.target.value })
          }
        />
      </div>
      <Handle type="source" position={Position.Bottom} isConnectable={true} />
    </div>
  );
}

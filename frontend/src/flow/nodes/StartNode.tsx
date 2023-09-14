import { Handle, NodeProps, Position } from "reactflow";
import useBoundStore, { StorageState } from "../lib/storage";
import * as R from "ramda";

import "./StartNode.css";
import { useCallback, useEffect } from "react";

export interface StartNodeData {
  inputPath: string;
}

const selector = (state: StorageState) => ({
  getNode: state.getNode<StartNodeData>,
  updateNodeData: state.updateNodeData<StartNodeData>,
});

export default function StartNode({ id }: NodeProps<StartNodeData>) {
  const { updateNodeData, getNode } = useBoundStore(selector);

  const node = getNode(id);
  const { inputPath } = R.pathOr<StartNodeData>(
    { inputPath: "" },
    ["data"],
    node
  );

  useEffect(() => {
    updateNodeData(id, { inputPath });
  }, []);

  const handleChangeInputPath = (evt: React.ChangeEvent<HTMLInputElement>) => {
    const inputPath = evt.target.value;
    updateNodeData(id, { inputPath });
  };

  return (
    <div className="node start-node">
      <div>
        <label htmlFor="inputPath">Input Path ($.):</label>
        <input
          id="inputPath"
          name="inputPath"
          value={inputPath}
          onChange={handleChangeInputPath}
        />
      </div>
      <Handle type="source" position={Position.Bottom} isConnectable={true} />
    </div>
  );
}

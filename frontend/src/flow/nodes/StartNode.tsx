import { Handle, NodeProps, Position } from "reactflow";
import useBoundStore, { StorageState } from "../lib/storage";

import "./StartNode.css";
import { useCallback } from "react";

export interface StartNodeData {
  inputPath: string;
}

const selector = (state: StorageState) => ({
  getNode: state.getNode<StartNodeData>,
  updateNodeData: state.updateNodeData<StartNodeData>,
});

export default function StartNode({ id }: NodeProps<StartNodeData>) {
  const { updateNodeData, getNode } = useBoundStore(selector);

  const handleChangeInputPath = (evt: React.ChangeEvent<HTMLInputElement>) => {
    const inputPath = evt.target.value;
    updateNodeData(id, { inputPath });
  };

  const onChangeInputPath = useCallback(handleChangeInputPath, []);

  return (
    <div className="node start-node">
      <div>
        <label htmlFor="inputPath">Input Path ($.):</label>
        <input
          id="inputPath"
          name="inputPath"
          value={getNode(id)?.data.inputPath}
          onChange={onChangeInputPath}
        />
      </div>
      <Handle type="source" position={Position.Bottom} isConnectable={true} />
    </div>
  );
}

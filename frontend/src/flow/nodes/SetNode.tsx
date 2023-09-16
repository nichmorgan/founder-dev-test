import { Handle, NodeProps, Position } from "reactflow";
import "./SetNode.css";
import useBoundStore, { StorageState } from "../lib/storage";
import * as R from "ramda";
import { useEffect } from "react";

export interface SetNodeData {
  path: string;
  value: string;
}

const selector = (state: StorageState) => ({
  getNode: state.getNode<SetNodeData>,
  updateNodeData: state.updateNodeData<SetNodeData>,
});

export default function SetNode({ id }: NodeProps<SetNodeData>) {
  const { updateNodeData, getNode } = useBoundStore(selector);

  const node = getNode(id);

  const path = R.pathOr("", ["data", "path"], node);
  const value = R.pathOr("", ["data", "value"], node);

  useEffect(() => {
    updateNodeData(id, { path, value });
  }, []);

  const onChangeCondition = (field: keyof SetNodeData, value: string) => {
    if (!node) return;
    const newData = R.assocPath(["data", field], value, node);
    updateNodeData(id, newData.data);
  };

  return (
    <div className="node if-node">
      <Handle type="target" position={Position.Top} isConnectable={true} />
      <div>
        <label htmlFor={`${id}_setPath`}>Set Path ($.):</label>
        <input
          id={`${id}_setPath`}
          name="setPath"
          value={path}
          onChange={(evt) => onChangeCondition("path", evt.target.value)}
        />

        <label htmlFor={`${id}_value`}>Value:</label>
        <input
          id={`${id}_value`}
          value={value}
          name="value"
          onChange={(evt) => onChangeCondition("value", evt.target.value)}
        />
      </div>
      <Handle type="source" position={Position.Bottom} isConnectable={true} />
    </div>
  );
}

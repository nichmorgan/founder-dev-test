import { Handle, NodeProps, Position } from "reactflow";
import "./SetNode.css";
import useBoundStore, { StorageState } from "../lib/storage";

export interface SetNodeData {
  path: string;
  value: unknown;
}

const selector = (state: StorageState) => ({
  updateNodeData: state.updateNodeData<SetNodeData>,
});

export default function SetNode({ id, data }: NodeProps<SetNodeData>) {
  const { updateNodeData } = useBoundStore(selector);

  const onChangeCondition = (field: keyof SetNodeData, value: unknown) => {
    Object.assign(data, { [field]: value });
    updateNodeData(id, data);
  };

  return (
    <div className="node if-node">
      <Handle type="target" position={Position.Top} isConnectable={true} />
      <div>
        <label htmlFor={`${id}_setPath`}>Set Path ($.):</label>
        <input
          id={`${id}_setPath`}
          name="setPath"
          defaultValue={""}
          onChange={(evt) => onChangeCondition("path", evt.target.value)}
        />

        <label htmlFor={`${id}_value`}>Value:</label>
        <input
          id={`${id}_value`}
          name="value"
          onChange={(evt) => onChangeCondition("value", evt.target.value)}
        />
      </div>
      <Handle type="source" position={Position.Bottom} isConnectable={true} />
    </div>
  );
}

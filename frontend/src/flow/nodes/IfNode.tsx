import { Handle, NodeProps, Position } from "reactflow";
import useBoundStore, { StorageState } from "../lib/storage";

import "./IfNode.css";
import { useState } from "react";

const OPERATORS_SET = new Set(["=", "<", "<=", ">=", ">"]);
export type IfOperator = typeof OPERATORS_SET;

export interface IfNodeCondition {
  path: string;
  operator: IfOperator;
  value: string;
}

export interface IfNodeData {
  condition: IfNodeCondition;
}

const selector = (state: StorageState) => ({
  updateNodeData: state.updateNodeData<IfNodeData>,
});

export default function IfNode({ id, data }: NodeProps<IfNodeData>) {
  const [state, setState] = useState({ condition: { ...data?.condition } });
  const { updateNodeData } = useBoundStore(selector);

  const onChangeCondition = (field: keyof IfNodeCondition, value: unknown) => {
    Object.assign(state.condition, { [field]: value });
    setState(state);
    updateNodeData(id, data);
  };

  return (
    <div className="node if-node">
      <Handle type="target" position={Position.Top} isConnectable={true} />
      <div>
        <label htmlFor={`${id}_inputPath`}>Input Path ($.):</label>
        <input
          id={`${id}_inputPath`}
          name="inputPath"
          defaultValue={""}
          onChange={(evt) => onChangeCondition("path", evt.target.value)}
        />

        <label htmlFor={`${id}_operator`}>Operator:</label>
        <select
          id={`${id}_operator`}
          name="operator"
          onChange={(evt) => onChangeCondition("operator", evt.target.value)}
        >
          {Array.from(OPERATORS_SET).map((operator) => (
            <option key={operator}>{operator}</option>
          ))}
        </select>

        <label htmlFor={`${id}_value`}>Value:</label>
        <input
          id={`${id}_value`}
          name="value"
          defaultValue={""}
          onChange={(evt) => onChangeCondition("value", evt.target.value)}
        />
      </div>
      <Handle
        id="Yes"
        type="source"
        position={Position.Right}
        title="Yes"
        style={{ background: "green" }}
      />
      <Handle
        id="No"
        type="source"
        position={Position.Left}
        title="No"
        style={{ background: "red" }}
      />
    </div>
  );
}

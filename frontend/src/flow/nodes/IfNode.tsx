import { Handle, NodeProps, Position } from "reactflow";
import useBoundStore, { StorageState } from "../lib/storage";
import * as R from "ramda";

import "./IfNode.css";

const OPERATORS_LIST = ["=", "<", "<=", ">=", ">"] as const;
export type IfOperator = (typeof OPERATORS_LIST)[number];

export interface IfNodeCondition {
  path: string;
  operator: IfOperator;
  value: string;
}

export interface IfNodeData {
  condition: IfNodeCondition;
}

const selector = (state: StorageState) => ({
  getNode: state.getNode,
  updateNodeData: state.updateNodeData<IfNodeData>,
});

export default function IfNode({ id }: NodeProps<Partial<IfNodeData>>) {
  const { getNode, updateNodeData } = useBoundStore(selector);
  const node = getNode<IfNodeData>(id);
  const { path, operator, value } = R.pathOr<IfNodeCondition>(
    { path: "", operator: "=", value: "" },
    ["data", "condition"],
    node
  );

  const onChangeCondition = (field: keyof IfNodeCondition, value: unknown) => {
    if (!node) return;
    const newData = R.assocPath(["data", "condition", field], value, node);
    updateNodeData(id, newData.data);
  };

  return (
    <div className="node if-node">
      <Handle type="target" position={Position.Top} isConnectable={true} />
      <div>
        <label htmlFor={`${id}_inputPath`}>Input Path ($.):</label>
        <input
          id={`${id}_inputPath`}
          name="inputPath"
          value={path}
          onChange={(evt) => onChangeCondition("path", evt.target.value)}
        />

        <label htmlFor={`${id}_operator`}>Operator:</label>
        <select
          id={`${id}_operator`}
          name="operator"
          value={operator}
          onChange={(evt) => onChangeCondition("operator", evt.target.value)}
        >
          {OPERATORS_LIST.map((operator) => (
            <option key={operator}>{operator}</option>
          ))}
        </select>

        <label htmlFor={`${id}_value`}>Value:</label>
        <input
          id={`${id}_value`}
          name="value"
          value={value}
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

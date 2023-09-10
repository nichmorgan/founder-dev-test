import { useCallback } from "react";
import { Handle, Position, WrapNodeProps } from "reactflow";

// import "./StartNode.css";

export interface StartNodeData {
  inputPath: string;
}

const DEFAULT_PROPS: Pick<WrapNodeProps<StartNodeData>, "data"> = {
  data: { inputPath: "" },
};

export default function StartNode({ data } = DEFAULT_PROPS) {
  const onChange = useCallback<React.ChangeEventHandler<HTMLInputElement>>(
    (event) => {
      event.preventDefault();
      data.inputPath = event.target.value;
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

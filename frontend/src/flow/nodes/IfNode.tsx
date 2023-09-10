export type IfOperator = "=" | "<" | "<=" | ">=" | ">";

export interface IfNodeCondition {
  path: string;
  operator: IfOperator;
}

export interface IfNodeData {
  conditions?: IfNodeCondition[];
}

export default function IfNode({}) {}

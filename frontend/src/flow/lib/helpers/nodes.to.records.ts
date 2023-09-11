import { Node } from "reactflow";

export default function nodesToRecords(nodes: Node[]): Record<string, Node> {
  const records: Record<string, Node> = {};

  nodes.forEach((node) => {
    Object.assign(records, { [node.id]: node });
  });

  return records;
}

import { StateCreator } from "zustand";
import { Node, NodeChange, OnNodesChange, applyNodeChanges } from "reactflow";

type NodesState = {
  nodes: Node[];
  appendNodes: (nodes: Node[]) => void;
  onNodesChange: OnNodesChange;
};

const createNodesSlice: StateCreator<NodesState> = (set, get) => ({
  nodes: [] as Node[],
  appendNodes: (nodes: Node[]) => {
    set({ nodes: get().nodes.concat(nodes) });
  },
  onNodesChange: (changes: NodeChange[]) => {
    set({ nodes: applyNodeChanges(changes, get().nodes) });
  },
});

export default createNodesSlice;
export type { NodesState };

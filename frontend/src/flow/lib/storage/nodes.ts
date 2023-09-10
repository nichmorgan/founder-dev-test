import { StateCreator } from "zustand";
import { Node, OnNodesChange, applyNodeChanges } from "reactflow";

type NodesState = {
  nodes: Node[];
  appendNodes: (nodes: Node[]) => void;
  onNodesChange: OnNodesChange;
  updateNodeData: <T>(nodeId: string, data: T) => void;
};

const createNodesSlice: StateCreator<NodesState> = (set, get) => ({
  nodes: [],
  appendNodes: (nodes) => {
    set({ nodes: get().nodes.concat(nodes) });
  },
  onNodesChange: (changes) => {
    set({ nodes: applyNodeChanges(changes, get().nodes) });
  },
  updateNodeData: <T>(nodeId: string, data: T) => {
    set({
      nodes: get().nodes.map((node) => {
        if (node.id === nodeId) {
          node.data = data;
        }
        return node;
      }),
    });
  },
});

export default createNodesSlice;
export type { NodesState };

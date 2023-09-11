import { StateCreator } from "zustand";
import { Node, OnNodesChange, applyNodeChanges } from "reactflow";
import nodesToRecords from "../helpers/nodes.to.records";

type NodesState = {
  nodes: Record<string, Node>;
  getNode: <T>(id: string) => Node<T> | null;
  setNodes: (nodes: Node[]) => void;
  appendNodes: (nodes: Node[]) => void;
  onNodesChange: OnNodesChange;
  updateNodeData: <T>(nodeId: string, data: T) => void;
};

const createNodesSlice: StateCreator<NodesState> = (set, get) => ({
  nodes: {},
  getNode(id) {
    return get().nodes[id] ?? null;
  },
  setNodes: (nodes) => {
    set({ nodes: nodesToRecords(nodes) });
  },
  appendNodes: (nodes) => {
    set({ nodes: { ...get().nodes, ...nodesToRecords(nodes) } });
  },
  onNodesChange: (changes) => {
    set({
      nodes: nodesToRecords(
        applyNodeChanges(changes, Object.values(get().nodes))
      ),
    });
  },
  updateNodeData: <T>(nodeId: string, data: T) => {
    const { nodes } = get();
    if (!nodes[nodeId]) return;
    set({ nodes: { ...get().nodes, [nodeId]: { ...nodes[nodeId], data } } });
  },
});

export default createNodesSlice;
export type { NodesState };

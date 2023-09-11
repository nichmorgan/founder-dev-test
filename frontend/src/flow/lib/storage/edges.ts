import { StateCreator } from "zustand";
import {
  Edge,
  OnConnect,
  OnEdgesChange,
  addEdge,
  applyEdgeChanges,
} from "reactflow";

type EdgesState = {
  edges: Edge[];
  setEdges: (edges: Edge[]) => void;
  onEdgesChange: OnEdgesChange;
  onConnect: OnConnect;
};

const createEdgesSlice: StateCreator<EdgesState> = (set, get) => ({
  edges: [],
  setEdges(edges) {
    set({ edges });
  },
  onEdgesChange: (changes) => {
    set({ edges: applyEdgeChanges(changes, get().edges) });
  },
  onConnect: (connection) => {
    set({ edges: addEdge(connection, get().edges) });
  },
});

export default createEdgesSlice;
export type { EdgesState };

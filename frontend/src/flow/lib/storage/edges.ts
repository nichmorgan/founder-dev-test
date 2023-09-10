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
  onEdgesChange: OnEdgesChange;
  onConnect: OnConnect;
};

const createEdgesSlice: StateCreator<EdgesState> = (set, get) => ({
  edges: [],
  onEdgesChange: (changes) => {
    set({ edges: applyEdgeChanges(changes, get().edges) });
  },
  onConnect: (connection) => {
    set({ edges: addEdge(connection, get().edges) });
  },
});

export default createEdgesSlice;
export type { EdgesState };
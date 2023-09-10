import { StateCreator } from "zustand";
import {
  Connection,
  Edge,
  EdgeChange,
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
  edges: [] as Edge[],
  onEdgesChange: (changes: EdgeChange[]) => {
    set({ edges: applyEdgeChanges(changes, get().edges) });
  },
  onConnect: (connection: Connection) => {
    set({ edges: addEdge(connection, get().edges) });
  },
});

export default createEdgesSlice;
export type { EdgesState };

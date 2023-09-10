import { create } from "zustand";
import createNodeSlice, { NodesState } from "./nodes";
import createEdgeSlice, { EdgesState } from "./edges";

type StorageState = NodesState & EdgesState;

const useBoundStore = create<StorageState>()((...operators) => ({
  ...createNodeSlice(...operators),
  ...createEdgeSlice(...operators),
}));

export default useBoundStore;
export type { StorageState };

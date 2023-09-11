import { create } from "zustand";
import createFLowSlice, { FlowState } from "./flow";
import createNodeSlice, { NodesState } from "./nodes";
import createEdgeSlice, { EdgesState } from "./edges";

type StorageState = NodesState & EdgesState & FlowState;

const useBoundStore = create<StorageState>()((...operators) => ({
  ...createNodeSlice(...operators),
  ...createEdgeSlice(...operators),
  ...createFLowSlice(...operators),
}));

export default useBoundStore;
export type { StorageState };

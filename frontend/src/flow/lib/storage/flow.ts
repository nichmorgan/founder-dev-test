import { ReactFlowInstance } from "reactflow";
import { StateCreator } from "zustand";

type FlowState = {
  flowInstance: ReactFlowInstance | null;
  setFlowInstance: (flowInstance: ReactFlowInstance) => void;
};

const createFLowSlice: StateCreator<FlowState> = (set) => ({
  flowInstance: null,
  setFlowInstance(flowInstance) {
    set({ flowInstance });
  },
});

export default createFLowSlice;
export type { FlowState };

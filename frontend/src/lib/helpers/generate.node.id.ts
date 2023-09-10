import { v4 as uuidv4 } from "uuid";

const generateNodeId = () => `node_${uuidv4()}`;
export default generateNodeId;

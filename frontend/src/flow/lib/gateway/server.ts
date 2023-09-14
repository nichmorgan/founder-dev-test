import { ReactFlowJsonObject } from "reactflow";
import axios, { AxiosInstance } from "axios";
import config from "../core/config";

export class ServerGateway {
  private readonly client: AxiosInstance;

  constructor(host: string = config.gatewayHost) {
    this.client = axios.create({ baseURL: host });
  }

  async getFlow(id: string): Promise<ReactFlowJsonObject> {
    const response = await this.client.get(`/flow/restore/${id}`);
    return response.data;
  }

  async saveFlow(id: string, flow: ReactFlowJsonObject): Promise<void> {
    const flowObj = { id, ...flow };
    await this.client.put("/flow/save", flowObj);
  }
}

export default new ServerGateway();

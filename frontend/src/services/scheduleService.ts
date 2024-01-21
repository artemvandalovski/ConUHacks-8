import { AxiosResponse } from "axios";
import http from "../constants/http";
import { Schedule } from "../models/schedule";

export const getScheduleByDate = async (date: string): Promise<any> => {
    const response: AxiosResponse<any> = await http.get(`/schedule/${date}`);
    return response.data;
}

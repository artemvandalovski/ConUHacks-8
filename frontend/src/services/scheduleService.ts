import { AxiosResponse } from "axios";
import http from "../apis/http";
import { Schedule } from "../models/schedule";

export const getScheduleByDate = async (date: string): Promise<Schedule> => {
    try {
        const response: AxiosResponse<Schedule> = await http.get(`/schedule/${date}`);
        return response.data;
    } catch (error) {
        return Promise.reject(error);
    }
};
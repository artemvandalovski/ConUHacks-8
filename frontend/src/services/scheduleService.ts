import { AxiosResponse } from "axios";
import http from "../constants/http";
import { Schedule } from "../models/schedule";

export const getScheduleByDate = async (date: string): Promise<Schedule> => {
    try {
        const response: AxiosResponse<Schedule> = await http.post("/schedule", { date });
        return response.data;
    } catch (error) {
        throw new Error("Failed to get schedule by date");
    }
};
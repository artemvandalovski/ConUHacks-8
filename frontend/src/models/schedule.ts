import { Vehicle } from "./vehicle";

export interface Appointment {
    start_time: string;
    end_time: string;
    vehicle: Vehicle;
}

export interface Bay {
    appointments: Appointment[];
}

export interface Schedule {
    date: string;
    profit: number;
    loss: number;
    bays: { [key: string]: Bay };
}
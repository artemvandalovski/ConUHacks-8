import { Vehicle } from "./vehicle";

export interface Appointment {
    start_time: string;
    end_time: string;
    vehicle: Vehicle;
}

export interface Bay {
    bay_type: string;
    appointments: Appointment[];
}

export interface Schedule {
    date: string;
    profit: number;
    loss: number;
    bays: Bay[];
}
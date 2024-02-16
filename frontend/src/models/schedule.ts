import { Vehicle } from "./vehicle";

export interface Appointment {
    vehicle: Vehicle;
    start_time: string;
    end_time: string;
}

export interface Bay {
    bay_type: string;
    appointments: Appointment[];
}

export enum BayType {
    COMPACT = "Compact",
    MEDIUM = "Medium",
    FULL_SIZE = "Full-size",
    CLASS_1_TRUCK = "Class 1 truck",
    CLASS_2_TRUCK = "Class 2 truck",
    FREE_STATION = "Any",
}

export function getBayTypeByString(vehicleType: string): BayType {
    for (const value of Object.values(BayType)) {
        if (value.toLowerCase() === vehicleType.toLowerCase()) {
            return value;
        }
    }
    return BayType.FREE_STATION;
}

export interface Schedule {
    date: string;
    profit: number;
    loss: number;
    bays: Bay[];
}
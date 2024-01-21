export interface Request {
    request_date: string;
    appointment_date: string;
    vehicle_type: string;
}

export interface Appointment {
    start_time: string;
    end_time: string;
    vehicle: string;
}

export class Bay {
    schedule: Appointment[];

    constructor() {
        this.schedule = [];
    }
}

export interface Schedule {
    date: string;
    profit: number;
    loss: number;
    bays: Record<string, Bay>;
}

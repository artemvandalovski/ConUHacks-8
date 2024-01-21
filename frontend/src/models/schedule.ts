export interface Appointment {
    start_time: string;
    end_time: string;
    vehicle: any;
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
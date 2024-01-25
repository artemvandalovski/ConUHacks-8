export interface Vehicle {
    vehicle_type: string;
    servicing_time: number;
    charge: number;
}

export enum VehicleType {
    COMPACT = "Compact",
    MEDIUM = "Medium",
    FULL_SIZE = "Full-size",
    CLASS_1_TRUCK = "Class 1 truck",
    CLASS_2_TRUCK = "Class 2 truck",
}

export const VehicleDetails: { [key in VehicleType]: { servicing_time: number, charge: number } } = {
    [VehicleType.COMPACT]: { servicing_time: 30, charge: 150 },
    [VehicleType.MEDIUM]: { servicing_time: 30, charge: 150 },
    [VehicleType.FULL_SIZE]: { servicing_time: 30, charge: 150 },
    [VehicleType.CLASS_1_TRUCK]: { servicing_time: 60, charge: 250 },
    [VehicleType.CLASS_2_TRUCK]: { servicing_time: 120, charge: 700 },
};
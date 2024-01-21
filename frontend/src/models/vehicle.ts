export class Vehicle {
    type: string;
    servicingTime: number;
    charge: number;

    constructor(vehicleType: string, servicingTime: number, charge: number) {
        this.type = vehicleType;
        this.servicingTime = servicingTime;
        this.charge = charge;
    }
}

export const VEHICLES: Vehicle[] = [
    new Vehicle("compact", 30, 150),
    new Vehicle("medium", 30, 150),
    new Vehicle("full-size", 30, 150),
    new Vehicle("class 1 truck", 60, 250),
    new Vehicle("class 2 truck", 120, 700),
];

export function getVehicleByType(vehicleType: string) {
    return VEHICLES.find(vehicle => vehicle.type === vehicleType);
}
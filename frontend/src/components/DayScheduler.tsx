import { useEffect, useState } from 'react';
import { styled } from '@mui/material/styles';
import Paper from '@mui/material/Paper';
import { ViewState } from '@devexpress/dx-react-scheduler';
import { Scheduler, DayView, Appointments, AppointmentTooltip, Resources } from '@devexpress/dx-react-scheduler-material-ui';
import { Schedule } from '../models/schedule';
import Select from '@mui/material/Select';
import MenuItem from '@mui/material/MenuItem';

const DayScheduler = ({ schedule }: { schedule: Schedule }) => {
    const [appointmentList, setAppointmentList] = useState<any[]>([]);

    useEffect(() => {
        const transformedAppointments = schedule.bays.map(bay => {
            return bay.appointments.map(appointment => ({
                startDate: appointment.start_time,
                endDate: appointment.end_time,
                title: appointment.vehicle.vehicle_type,
            }));
        }).flat();
        setAppointmentList(transformedAppointments);

    }, [schedule]);

    return (
        <Paper>
            <Scheduler
                data={appointmentList}
            >
                <ViewState
                    currentDate={appointmentList[0]?.startDate}
                />
                <DayView
                    startDayHour={7}
                    endDayHour={19}
                />
                <Appointments />
                <AppointmentTooltip />
            </Scheduler>
        </Paper>
    );
}

export default DayScheduler;
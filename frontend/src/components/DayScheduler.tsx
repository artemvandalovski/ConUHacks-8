import { useEffect, useState } from 'react';
import Paper from '@mui/material/Paper';
import { ViewState } from '@devexpress/dx-react-scheduler';
import { Scheduler, DayView, Appointments, AppointmentTooltip } from '@devexpress/dx-react-scheduler-material-ui';
import { Appointment } from '../models/schedule';

// TODO: Create new appointments with https://devexpress.github.io/devextreme-reactive/react/scheduler/docs/guides/editing/
const DayScheduler = ({ appointments }: { appointments: Appointment[] }) => {
    const [appointmentList, setAppointmentList] = useState<any[]>([]);

    useEffect(() => {
        const transformedAppointments = appointments.map(appointment => ({
            startDate: appointment.start_time,
            endDate: appointment.end_time,
            title: appointment.vehicle.type,
        }));
        setAppointmentList(transformedAppointments);
    }, [appointments]);

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
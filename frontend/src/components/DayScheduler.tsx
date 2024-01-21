import Paper from '@mui/material/Paper';
import { ViewState, EditingState, IntegratedEditing } from '@devexpress/dx-react-scheduler';
import { Scheduler, DayView, Appointments, AppointmentForm, AppointmentTooltip, ConfirmationDialog } from '@devexpress/dx-react-scheduler-material-ui';
import { Appointment, Schedule } from '../models/schedule';


// TODO: https://devexpress.github.io/devextreme-reactive/react/scheduler/docs/guides/editing/
const DayScheduler = ({ schedule }: { schedule: Schedule | null }) => {
    // const appointments2: Appointment[] = [];
    if (schedule) {
        Object.keys(schedule.bays).forEach((bayKey, bayIndex) => {
            const bay = schedule.bays[bayKey];
            bay.appointments.forEach((appointment, appointmentIndex) => {
                appointments2.push({
                    id: `${bayIndex}-${appointmentIndex}`,
                    title: `Bay ${bayIndex + 1}`,
                    startDate: new Date(`${schedule.date}T${appointment.startTime}`),
                    endDate: new Date(`${schedule.date}T${appointment.endTime}`),
                });
            });
        });
    }

    // const convertedAppointments = appointments.map(appointment => ({
    //     startDate: appointment.start_time,
    //     endDate: appointment.end_time,
    //     title: appointment.vehicle.type,
    // }));

    const appointments2 = [
        { startDate: '2021-10-04T09:45', endDate: '2021-10-04T11:00', title: 'Meeting' },
        { startDate: '2021-10-04T12:00', endDate: '2021-10-04T13:30', title: 'Go to a gym' },
    ];



    return (
        <Paper>
            <Scheduler
                data={appointments2}
            >
                <ViewState
                    currentDate="2021-10-04"
                />
                <DayView
                    startDayHour={7}
                    endDayHour={19}
                />
                <Appointments appointmentComponent={Appointment} />
                <AppointmentTooltip />
            </Scheduler>
        </Paper>
    );
}

export default DayScheduler;
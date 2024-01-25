import { useEffect, useState } from 'react';
import Paper from '@mui/material/Paper';
import {
    ViewState, GroupingState, IntegratedGrouping, IntegratedEditing, EditingState,
} from '@devexpress/dx-react-scheduler';
import {
    Scheduler,
    Resources,
    Appointments,
    AppointmentTooltip,
    GroupingPanel,
    DayView,
    DragDropProvider,
    AppointmentForm,
} from '@devexpress/dx-react-scheduler-material-ui';
import { BayType, Schedule, getBayTypeByString } from '../models/schedule';

const DayScheduler = ({ schedule }: { schedule: Schedule }) => {
    const [appointmentList, setAppointmentList] = useState<any[]>([]);

    useEffect(() => {
        const transformedAppointments = schedule.bays.map(bay => {
            return bay.appointments.map(appointment => ({
                title: getBayTypeByString(appointment.vehicle.vehicle_type),
                bayType: getBayTypeByString(bay.bay_type),
                startDate: appointment.start_time,
                endDate: appointment.end_time,
            }));
        }).flat();
        setAppointmentList(transformedAppointments);

    }, [schedule]);

    const bays = Object.keys(BayType).map(key => ({
        id: BayType[key as keyof typeof BayType],
        text: BayType[key as keyof typeof BayType],
    }));


    const resources = [{
        fieldName: 'bayType',
        title: 'Bay Type',
        instances: bays,
    }];

    return (
        <Paper>
            <Scheduler data={appointmentList}>
                <ViewState defaultCurrentDate={schedule.date} />
                <EditingState onCommitChanges={() => { }} />
                <GroupingState grouping={[{ resourceName: 'bayType' }]} />

                <DayView startDayHour={7} endDayHour={19} />
                <Appointments />
                <Resources data={resources} mainResourceName="bayType" />

                <IntegratedGrouping />
                <IntegratedEditing />

                <AppointmentTooltip showOpenButton />
                <AppointmentForm />
                <GroupingPanel />
                <DragDropProvider />
            </Scheduler>
        </Paper>
    );
}

export default DayScheduler;
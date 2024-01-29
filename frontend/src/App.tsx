import { useEffect, useState } from 'react';
import './App.css';
import { getScheduleByDate } from './services/scheduleService';
import { Schedule } from './models/schedule';
import DayScheduler from './components/DayScheduler';
import { Container, Grid, MantineProvider } from '@mantine/core';
import { DatePicker } from '@mantine/dates';

function App() {
  const DEFAULT_DATE = new Date(2022, 9);
  const [date, setDate] = useState<Date | null>(DEFAULT_DATE);
  const [schedule, setSchedule] = useState<Schedule>();

  useEffect(() => {
    if (date) {
      getScheduleByDate(date.toISOString().split('T')[0]).then((schedule: Schedule) => {
        schedule.bays.forEach(bay =>
          console.log(bay.appointments.length)
        );
        setSchedule(schedule);
      });
    }
  }, [date]);

  return (
    <MantineProvider>
      <Container fluid>
        <Grid>
          <Grid.Col span={6}>
            <DatePicker value={date} onChange={setDate} defaultDate={DEFAULT_DATE} />
          </Grid.Col>
          <Grid.Col span={6}>
            {/* {schedule && <DayScheduler schedule={schedule} />} */}
          </Grid.Col>
        </Grid>
      </Container>
    </MantineProvider>
  );
}

export default App;

import React, { useEffect, useState } from 'react';
import './App.css';
import { getScheduleByDate } from './services/scheduleService';
import { Schedule } from './models/schedule';
import DayScheduler from './components/DayScheduler';
import { Container, Grid, MantineProvider } from '@mantine/core';
import { DateTimePicker } from '@mantine/dates';

function App() {

  const [date, setDate] = useState<Date | null>(null);
  const [schedule, setSchedule] = useState<Schedule>();

  useEffect(() => {
    if (date) {
      getScheduleByDate(date.toISOString().split('T')[0]).then((schedule: Schedule) => {
        setSchedule(schedule);
      });
    }
  }, [date]);

  return (
    <MantineProvider>
      <Container fluid>
        <Grid>
          <Grid.Col span={6}>
            <DateTimePicker label="Pick date and time" placeholder="Pick date and time" value={date} onChange={setDate} />
          </Grid.Col>
          <Grid.Col span={6}>
            {schedule && <DayScheduler schedule={schedule} />}
          </Grid.Col>
        </Grid>
      </Container>
    </MantineProvider>
  );
}

export default App;

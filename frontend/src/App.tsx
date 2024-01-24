import React, { useEffect, useState } from 'react';
import './App.css';
import { getScheduleByDate } from './services/scheduleService';
import { Schedule } from './models/schedule';
import DayScheduler from './components/DayScheduler';
import { Container, Grid, MantineProvider } from '@mantine/core';
import { DateTimePicker } from '@mantine/dates';

function App() {

  const [schedule, setSchedule] = useState<Schedule>();

  useEffect(() => {
    getScheduleByDate('2022-10-05').then((schedule: Schedule) => {
      setSchedule(schedule);
    });
  }, []);

  return (
    <MantineProvider>
      <Container fluid>
        <Grid>
          <Grid.Col span={6}>
            <DateTimePicker label="Pick date and time" placeholder="Pick date and time" />
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

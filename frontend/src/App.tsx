import React, { useEffect, useState } from 'react';
import './App.css';
import { Box, Button } from '@mui/material';
import { getScheduleByDate } from './services/scheduleService';
import { Schedule } from './models/schedule';

function App() {

  const [schedule, setSchedule] = useState<Schedule>();

  useEffect(() => {
    getScheduleByDate('2022-10-05').then((schedule: Schedule) => {
      setSchedule(schedule);
    });
  }, []);

  return (
    <Box sx={{ display: 'flex', justifyContent: 'center', alignItems: 'center', height: '100vh' }}>
      <Button variant="contained">Hello World</Button>
    </Box>
  );
}

export default App;

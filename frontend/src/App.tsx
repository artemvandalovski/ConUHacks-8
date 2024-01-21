import React, { useState, useEffect } from 'react';
import SelectionCalendar from './components/SelectionCalendar';
import Dashboard from './components/Dashboard';
import { getScheduleByDate } from './services/scheduleService';
import { Schedule } from './models/schedule';
import DayScheduler from './components/DayScheduler';


const App: React.FC = () => {
  const [selectedDate, setSelectedDate] = useState<Date | null>(new Date('2022-10-04'));
  const [schedule, setSchedule] = useState<Schedule | null>(null);

  useEffect(() => {
    if (selectedDate) {
      getScheduleByDate(selectedDate.toLocaleDateString()).then((schedule: Schedule) => {
        setSchedule(schedule);
      });
    }
  }, [selectedDate]);

  const handleDateSelect = (date: Date) => {
    setSelectedDate(date);
  };

  return (
    <div className="App" style={{ display: 'flex', height: '100vh' }}>
      <div style={{ width: '50%', display: 'flex', flexDirection: 'column' }}>
        <div style={{ flex: 1 }}>
          <SelectionCalendar onSelectDate={handleDateSelect} />
        </div>
        <div style={{ flex: 1 }}>
          <Dashboard />
        </div>
      </div>
      <div style={{ width: '50%', overflow: 'auto' }}>
        <DayScheduler schedule={schedule} />
      </div>
    </div>
  );
}

export default App;

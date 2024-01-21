import React, { useState, useEffect } from 'react';
import SelectionCalendar from './components/SelectionCalendar';
import Dashboard from './components/Dashboard';
import { getScheduleByDate } from './services/scheduleService';
import { Schedule } from './models/schedule';
import DayScheduler from './components/DayScheduler';
import Select from 'react-select'

const CARS_OPTIONS = [
  { value: 'compact', label: 'Compact Car' },
  { value: 'medium', label: 'Medium Car' },
  { value: 'full-size', label: 'Full-size Car' },
  { value: 'class 1 truck', label: 'Class 1 Truck' },
  { value: 'class 2 truck', label: 'Class 2 Truck' },
]

const App: React.FC = () => {
  const [selectedDate, setSelectedDate] = useState<Date | null>(null);
  const [selectedCarType, setSelectedCarType] = useState<string>("");
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
          <div style={{ padding: 10 }}>
            {selectedDate && <Select options={CARS_OPTIONS} onChange={(selectedOption) => setSelectedCarType(selectedOption?.value || "")} />}
          </div>
        </div>
        <div style={{ flex: 1 }}>
          <Dashboard />
        </div>
      </div>
      <div style={{ width: '50%', overflow: 'auto' }}>
        {selectedCarType && schedule && <DayScheduler appointments={schedule.bays[selectedCarType].appointments} />}
      </div>
    </div>
  );
}

export default App;

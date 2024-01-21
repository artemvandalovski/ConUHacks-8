import React, { useState } from 'react';
import SelectionCalendar from './components/SelectionCalendar';
import DayViewCalendar from './components/DayViewCalendar';
import Dashboard from './components/Dashboard';

const App: React.FC = () => {
  const [selectedDate, setSelectedDate] = useState<Date | null>(null);

  const handleDateSelect = (date: Date) => {
    setSelectedDate(date);
    // You can perform additional actions when a date is selected
  };

  return (
    <div className="App" style={{ display: 'flex', height: '100vh' }}>
      <div style={{ width: '50%', display: 'flex', flexDirection: 'column' }}>
        <div style={{ flex: 1 }}>
          <h1>Scheduling App</h1>
          <SelectionCalendar onSelectDate={handleDateSelect} />
          {selectedDate && (
            <p>Selected Date: {selectedDate.toDateString()}</p>
          )}
        </div>
        <div style={{ flex: 1 }}>
          <Dashboard />
        </div>
      </div>
      <div style={{ width: '50%', overflow: 'auto' }}>
        <DayViewCalendar />
      </div>
    </div>
  );
};

export default App;

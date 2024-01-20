import React, { useState } from 'react';
import SelectionCalendar from './components/SelectionCalendar';
import DayViewCalendar from './components/DayViewCalendar';

const App: React.FC = () => {
  const [selectedDate, setSelectedDate] = useState<Date | null>(null);

  const handleDateSelect = (date: Date) => {
    setSelectedDate(date);
    // You can perform additional actions when a date is selected
  };

  return (
    <div className="App" style={{ display: 'flex', flexDirection: 'row' }}>
      <div>
        <h1>Scheduling App</h1>
        <SelectionCalendar onSelectDate={handleDateSelect} />
        {selectedDate && (
          <p>Selected Date: {selectedDate.toDateString()}</p>
        )}
      </div>
      <div>
        <DayViewCalendar />
      </div>
    </div>
  );
};

export default App;

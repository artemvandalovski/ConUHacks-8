import React, { useState } from 'react';
import SelectionCalendar from './components/SelectionCalendar';

const App: React.FC = () => {
  const [selectedDate, setSelectedDate] = useState<Date | null>(null);

  const handleDateSelect = (date: Date) => {
    setSelectedDate(date);
    // You can perform additional actions when a date is selected
  };

  return (
    <div className="App">
      <h1>Scheduling App</h1>
      <SelectionCalendar onSelectDate={handleDateSelect} />
      {selectedDate && (
        <p>Selected Date: {selectedDate.toDateString()}</p>
      )}
    </div>
  );
};

export default App;

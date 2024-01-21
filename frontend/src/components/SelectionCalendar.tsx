import React, { useState } from 'react';
import Calendar from 'react-calendar';
import 'react-calendar/dist/Calendar.css';
import './SelectionCalendar.css'; // Assuming you'll create this CSS file

interface CalendarProps {
  onSelectDate: (date: Date) => void;
}

const SelectionCalendar: React.FC<CalendarProps> = ({ onSelectDate }) => {
  const [selectedDate, setSelectedDate] = useState<Date | Date[] | null>(new Date());

  const handleDateChange = (date: Date | Date[] | null) => {
    if (date) {
      setSelectedDate(date);
      onSelectDate(date instanceof Date ? date : (date as Date[])[0]);
    }
  };

  return (
    <div className="calendar-container">
      <Calendar
        onChange={handleDateChange as any}
        value={selectedDate instanceof Date ? selectedDate : undefined}
        calendarType="gregory"
      />
    </div>
  );
};

export default SelectionCalendar;

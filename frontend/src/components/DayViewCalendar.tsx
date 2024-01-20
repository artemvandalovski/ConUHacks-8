import React, { useState, useEffect } from 'react';

const initialAvailability = { startTime: '07:00', endTime: '19:00' };
const totalHours = 12; // Total hours from 7 am to 7 pm
const barHeight = 240; // Set the height of the vertical bar
const timeSlotHeight = barHeight / totalHours;

const DayViewCalendar = () => {
  const [schedules, setSchedules] = useState(
    new Array(10).fill([]).map(() => [initialAvailability])
  );

  const timeRangesPerBay = [
    [[8, 10], [11, 13], [14, 15.5], [9, 18]],
    [[8, 11], [14, 16]],
    [[8, 10.5], [11, 14]],
    // Add more time ranges for other bays as needed
  ];

  // Function to convert numeric time to HH:mm format
  const formatTime = (time: any) => {
    const hours = Math.floor(time);
    const minutes = Math.round((time - hours) * 60);
    return `${hours.toString().padStart(2, '0')}:${minutes.toString().padStart(2, '0')}`;
  };

  // Function to update schedules with time ranges
  const updateSchedules = () => {
    setSchedules((prevSchedules) => {
      const newSchedules = new Array(10).fill([]).map(() => []);

      timeRangesPerBay.forEach((timeRanges, bayIndex) => {
        timeRanges.forEach(([start, end]) => {
          const startTime = formatTime(start);
          const endTime = formatTime(end);
          newSchedules[bayIndex].push({ startTime, endTime } as never);
        });
      });

      return newSchedules;
    });
  };

  useEffect(() => {
    // Uncomment the line below to update schedules with the time ranges
    updateSchedules();
  }, []); // Empty dependency array ensures the effect runs once after the initial render

  return (
    <div style={{ display: 'grid', gridTemplateColumns: 'repeat(10, 1fr)', gap: '8px' }}>
      {/* Bay columns */}
      {schedules.map((baySchedule, bayIndex) => (
        <div key={bayIndex} style={{ border: '1px solid #ddd', padding: '8px' }}>
          <div style={{ backgroundColor: '#f2f2f2', fontWeight: 'bold', padding: '8px' }}>{`Bay ${bayIndex + 1}`}</div>
          {/* Progress bar for each bay */}
          <div style={{ position: 'relative', marginTop: '8px' }}>
            {/* Red bar for allocated time */}
            {baySchedule.map((booking, index) => (
              <div
                key={index}
                style={{
                  position: 'absolute',
                  top: `${(parseInt(booking.startTime.split(':')[0], 10) - 7) * timeSlotHeight}px`,
                  height: `${(parseInt(booking.endTime.split(':')[0], 10) - parseInt(booking.startTime.split(':')[0], 10)) * timeSlotHeight}px`,
                  backgroundColor: '#dc3545', // Red color
                  width: '100%',
                }}
              ></div>
            ))}
            {/* Blue bar for the entire day */}
            <div
              style={{
                position: 'absolute',
                top: '0',
                height: '100%',
                backgroundColor: '#007bff', // Blue color
                width: '100%',
              }}
            ></div>
          </div>
        </div>
      ))}
    </div>
  );
};

export default DayViewCalendar;

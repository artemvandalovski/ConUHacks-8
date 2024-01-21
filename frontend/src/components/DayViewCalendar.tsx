import React, { useState, useEffect } from 'react';
import { Container, Row, Col, Card } from 'react-bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css'; // Import Bootstrap CSS

const initialAvailability = { startTime: '07:00', endTime: '19:00' };
const totalHours = 12; // Total hours from 7 am to 7 pm
const barHeight = 240; // Set the height of the vertical bar
const timeSlotHeight = barHeight / totalHours;

const DayViewCalendar = () => {
  const [schedules, setSchedules] = useState(
    new Array(10).fill([]).map(() => [initialAvailability])
  );

  const timeRangesPerBay = [
    [[8, 10], [11, 13], [14, 15.5], [16, 18]],
    [[8, 11], [14, 16]],
    [[8, 10.5], [11, 14]],
    // Add more time ranges for other bays as needed
  ];

  const formatTime = (time: any) => {
    const hours = Math.floor(time);
    const minutes = Math.round((time - hours) * 60);
    return `${hours.toString().padStart(2, '0')}:${minutes.toString().padStart(2, '0')}`;
  };

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
    updateSchedules();
  }, []);

  return (
    <Container className="mt-3">
      <Row className="justify-content-md-center">
        {schedules.map((baySchedule, bayIndex) => (
          <Col key={bayIndex} className="mb-4" style={{ flex: 0, maxWidth: '10%' }}> {/* Inline styles for equal width */}
            <Card>
              <Card.Header className="bg-primary text-white">
                {`Bay ${bayIndex + 1}`}
              </Card.Header>
              <Card.Body className="p-2" style={{ position: 'relative', height: `${barHeight}px`, padding: 0 }}>
                {/* Blue bar for the entire day */}
                <div className="bg-info" style={{ position: 'absolute', top: 0, left: 0, right: 0, bottom: 0 }}></div>
                {/* Red bar for allocated time */}
                {baySchedule.map((booking, index) => (
                  <div
                    key={index}
                    className="bg-danger"
                    style={{
                      position: 'absolute',
                      top: `${(parseInt(booking.startTime.split(':')[0], 10) - 7) * timeSlotHeight}px`,
                      height: `${(parseInt(booking.endTime.split(':')[0], 10) - parseInt(booking.startTime.split(':')[0], 10)) * timeSlotHeight}px`,
                      left: 0,
                      right: 0,
                    }}
                  ></div>
                ))}
              </Card.Body>

            </Card>
          </Col>
        ))}
      </Row>
    </Container>


  );
};

export default DayViewCalendar;

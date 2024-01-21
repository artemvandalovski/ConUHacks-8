import React from 'react';
import CumulativeProfitOverview from './CumulativeProfitOverview';
import './Dashboard.css'; // Make sure to create this CSS file for styling

const Dashboard = () => {
  return (
    <div className="dashboard">
      <div className="chart-box">
        <CumulativeProfitOverview />
        <div className="chart-info">
          <div className="chart-text">
            <h2>PROFIT</h2>
            <p>1.2 M</p>
          </div>
          <div className="chart-stats">
            <p>Cumulative Loss: 300k</p>
            <p>Daily Loss: 16k</p>
          </div>
        </div>
      </div>
      <div className="data-list">
        <h3>Daily Revenue Chart</h3>
        <ul>
          <li>Compact Cars: 10k</li>
          <li>Medium Cars: 35k</li>
          <li>Full-Size Cars: 100k</li>
          <li>Class 1 Trucks: 100k</li>
          <li>Class 2 Trucks: 100k</li>
        </ul>
      </div>
    </div>
  );
};

export default Dashboard;

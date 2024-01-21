import React, { useState } from 'react';
import { PieChart, Pie, Cell, Legend, Label, Sector } from 'recharts';

const data = [
  { name: 'Compact Cars', value: 10000 },
  { name: 'Medium Cars', value: 35000 },
  { name: 'Full-sized Cars', value: 100000 },
  { name: 'Class 1 Trucks', value: 100000 },
  { name: 'Class 2 Trucks', value: 100000 },
];

const COLORS = ['#0088FE', '#00C49F', '#FFBB28', '#FF8042', '#FF8042'];

const renderActiveShape = (props: any) => {
  const { cx, cy, innerRadius, outerRadius, startAngle, endAngle, fill } = props;
  return (
    <Sector
      cx={cx}
      cy={cy}
      innerRadius={innerRadius}
      outerRadius={outerRadius + 10} // Increase the outer radius for hover effect
      startAngle={startAngle}
      endAngle={endAngle}
      fill={fill}
    />
  );
};

const CumulativeProfitOverview = () => {
  const [activeIndex, setActiveIndex] = useState(null);

  const onPieEnter = (_: any, index: any) => {
    setActiveIndex(index);
  };

  const onPieLeave = () => {
    setActiveIndex(null);
  };

  return (
    <PieChart width={400} height={300}>
      <Pie
        activeIndex={activeIndex!}
        activeShape={renderActiveShape} // Render a custom active shape on hover
        data={data}
        cx={100}
        cy={120}
        innerRadius={60}
        outerRadius={100}
        fill="#8884d8"
        dataKey="value"
        onMouseEnter={onPieEnter}
        onMouseLeave={onPieLeave}
      >
        <Label
          value="PROFIT 1.2 M"
          position="center"
          style={{ textAnchor: 'middle', fontSize: '1.5em', fill: '#fff' }}
        />
        {data.map((entry, index) => (
          <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />
        ))}
      </Pie>
      <Legend />
    </PieChart>
  );
};

export default CumulativeProfitOverview;

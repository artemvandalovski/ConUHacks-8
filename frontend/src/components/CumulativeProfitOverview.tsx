import React, { useState } from 'react';
import { PieChart, Pie, Cell, Legend, Sector } from 'recharts';

const data = [
  { name: 'Compact Cars', value: 10000 },
  { name: 'Medium Cars', value: 35000 },
  { name: 'Full-sized Cars', value: 100000 },
  { name: 'Class 1 Trucks', value: 100000 },
  { name: 'Class 2 Trucks', value: 100000 },
];

const COLORS = ['#0088FE', '#00C49F', '#FFBB28', '#FF8042', '#FF8042'];

const renderActiveShape = (props: any) => {
  const { cx, cy, innerRadius, outerRadius, startAngle, endAngle, fill, payload, percent, value } = props;
  return (
    <Sector
      cx={cx}
      cy={cy}
      innerRadius={innerRadius}
      outerRadius={outerRadius + 10} // Increase the outer radius to make the slice pop out
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
    <PieChart width={400} height={400}>
      <Pie
        activeIndex={activeIndex!}
        activeShape={renderActiveShape} // This will render the custom active shape
        data={data}
        cx={200}
        cy={200}
        innerRadius={120}
        outerRadius={160}
        fill="#8884d8"
        dataKey="value"
        onMouseEnter={onPieEnter}
        onMouseLeave={onPieLeave}
      >
        {data.map((entry, index) => (
          <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />
        ))}
      </Pie>
      <Legend />
    </PieChart>
  );
};

export default CumulativeProfitOverview;

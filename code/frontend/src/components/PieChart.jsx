import React, { useState, useEffect } from 'react';
import { VictoryPie } from 'victory';

const wantedGraphicData = [{ y: 10 }, { y: 50 }, { y: 40 }]; // Data that we want to display
const defaultGraphicData = [{ y: 0 }, { y: 0 }, { y: 100 }];

const graphicColor = ['#388087', '#6fb3b8', '#badfe7']; // Colors


export default function PieChart() {
    const [graphicData, setGraphicData] = useState(defaultGraphicData);

  useEffect(() => {
    setGraphicData(wantedGraphicData); // Setting the data that we want to display
  }, []);
   return(
    <VictoryPie
    animate={{ easing: 'exp' }}
        data={graphicData}
        width={250}
        height={250}
        colorScale={graphicColor}
        innerRadius={50}
    />
   );
}
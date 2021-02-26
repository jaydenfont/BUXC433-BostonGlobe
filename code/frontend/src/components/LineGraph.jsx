import React from "react";
import { VictoryChart, VictoryArea, VictoryTheme, VictoryLabel} from "victory"; 

const data = [
  { x: "2015", y: 6 },
  { x: "2016", y: 13 },
  { x: "2017", y: 17 },
  { x: "2018", y: 26 },
  { x: "2019", y: 38 }
];


const data2 = [
  { x: "2015", y: 12 },
  { x: "2016", y: 26 },
  { x: "2017", y: 34 },
  { x: "2018", y: 32 },
  { x: "2019", y: 76 }
];

const data3 = [
  { x: "2015", y: 18 },
  { x: "2016", y: 32 },
  { x: "2017", y: 40 },
  { x: "2018", y: 38 },
  { x: "2019", y: 82 }
];

const colors = {
  teal: "hsl(174, 100%, 29%)",
  blueGrey: "#607D8B",
  lightGrey: "#eee"
};

export default function LineGraph() {
  return (
    <div style={{ maxWidth: "800px", margin: "0 auto" }}>
      <VictoryChart theme={VictoryTheme.material} width={800} height={400}>
        <VictoryArea
         labelComponent={<VictoryLabel dy={30} />}
        interpolation="natural"
          data={data}
          labels={({ datum }) => datum.y}
          style={{ data: { fill: colors.teal, fillOpacity: 0.7 } }}
        />
        <VictoryArea
        interpolation="natural"
          data={data2}
          labels={({ datum}) => datum.y}
          style={{ data: { fill: colors.teal, fillOpacity: 0.5 } }}
        />

<VictoryArea
        interpolation="natural"
          data={data3}
          labels={({ datum}) => datum.y}
          style={{ data: { fill: colors.teal, fillOpacity: 0.3 } }}
        />
      </VictoryChart>
    </div>
  );
}
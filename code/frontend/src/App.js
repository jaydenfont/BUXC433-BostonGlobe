import React from "react";
import {LineGraph, PieChart, BarGraph} from "./components"

function App() {
  return (
    <div>
    <div style={{ maxWidth: "800px", margin: "0 auto" }}>
     <LineGraph/>
    </div>
    <div style={{ maxWidth: "800px", margin: "0 auto" }}>
     <PieChart/>
    </div>
    <div style={{ maxWidth: "800px", margin: "0 auto" }}>
     <BarGraph/>
    </div>
    </div>
    
  );
}


export default App
import React from "react";
import {useRef, useState} from "react";
import "./Plant.css";

export default function Plant() {
  

  const [inputs, setInputs] = useState({});

  const handleChange = (event) => {
    const name = event.target.name;
    const value = event.target.value;
    setInputs(values => ({...values, [name]: value}))
  }

  const handleSubmit = (event) => {
    event.preventDefault();
    alert(inputs);
  }


  
  return (
    <main id="plant">
      <h1>Plant</h1>
      <h3>Input an plant into the simulation</h3>
      <form onSubmit={handleSubmit}>
        
          <div id = "type">
                <label> Plant type:
                <input 
                type="text"
                name = "plantType"
                value = {inputs.plantType || ""}
                onChange = {handleChange}
                />
                </label>
            </div>

            <div id = "name">
                <label> Growth Rate
                <input 
                type="text"
                name = "growthRate"
                value = {inputs.growthRate || ""}
                onChange = {handleChange}
                />
                </label>
            </div>

            <div id = "max">

                <label> Max Height
                <input 
                type="text"
                name = "maxHeight"
                value = {inputs.maxHeight|| ""}
                onChange= {handleChange}
                />
                </label>
            </div>
        
          
      
      <div id = "Percip">
              <label> Ideal Percipitation
              <input 
              type="text"
              name = "percip"
              value = {inputs.percip|| ""}
              onChange= {handleChange}
              />
              </label>
          </div>

          <div id = "Temp">
              <label> Ideal Temperature
              <input 
              type="text"
              name = "temp"
              value = {inputs.temp|| ""}
              onChange= {handleChange}
              />
              </label>
          </div>
          <div id = "lifeSpan">
              <label> Life Span
              <input 
              type="text"
              name = "lifeSpan"
              value = {inputs.LifeSpan|| ""}
              onChange= {handleChange}
              />
            </label>
          </div>
          
      
          
          <div id = "Shade">
              <label> Shade Tolerance
              <input 
              type="text"
              name = "shadeTol"
              value = {inputs.shadeTol|| ""}
              onChange= {handleChange}
              />
              </label>
          </div>
        
          <div id = "seedsProduced">
              <label> Seeds Produced
              <input 
              type="text"
              name = "seedsProduced"
              value = {inputs.seedProduced|| ""}
              onChange= {handleChange}
              />
              </label>
          </div>
          <div id = "seedsProduction">
              <label> Seeds Production
              <input 
              type="text"
              name = "sedsProduction"
              value = {inputs.seedProduction|| ""}
              onChange= {handleChange}
              />
              </label>
          </div>
          
     

          

          
          <input type="submit" />
        
        
         


      </form>

    </main>
  );
}

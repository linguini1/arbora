import React from "react";
import {useState} from "react";

export default function Envir() {
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
    <main id="Envir">
      <h1>Envinomentr</h1>
      <h3>Input an envinroment into the simulation</h3>

      <form onSubmit={handleSubmit}>
        <div id = "Temperature">
            <label> Month 1:
            <input 
            type="text"
            name = "temp1"
            value = {inputs.temp1 || ""}
            onChange = {handleChange}
            />
            </label>

            <label> Growth Rate
            <input 
            type="text"
            name = "growthRate"
            value = {inputs.growthRate || ""}
            onChange = {handleChange}
            />
            </label>
        </div>

        <div id = "Percip">
            <label> Growth Rate
            <input 
            type="text"
            name = "growthRate"
            value = {inputs.growthRate || ""}
            onChange = {handleChange}
            />
            </label>

            <label> Max Height
            <input 
            type="text"
            name = "maxHeight"
            value = {inputs.maxHeight|| ""}
            onChange= {handleChange}
            />
            </label>

            <label> Shade Tolerance
            <input 
            type="text"
            name = "shadeTol"
            value = {inputs.shadeTol|| ""}
            onChange= {handleChange}
            />
            </label>

            <label> Ideal Percipitation
            <input 
            type="text"
            name = "percip"
            value = {inputs.percip|| ""}
            onChange= {handleChange}
            />
            </label>

            <label> Ideal Temperature
            <input 
            type="text"
            name = "temp"
            value = {inputs.temp|| ""}
            onChange= {handleChange}
            />
            </label>

            <label> Seeds Produced
            <input 
            type="text"
            name = "seedsProduced"
            value = {inputs.seedProduced|| ""}
            onChange= {handleChange}
            />
            </label>

            <label> Seeds Production
            <input 
            type="text"
            name = "sedsProduction"
            value = {inputs.seedProduction|| ""}
            onChange= {handleChange}
            />
            </label>

            <label> Life Span
            <input 
            type="text"
            name = "lifeSpan"
            value = {inputs.LifeSpan|| ""}
            onChange= {handleChange}
            />
          </label>
        </div>
        <input type="submit" />


      </form>

      
    </main>
  );
}

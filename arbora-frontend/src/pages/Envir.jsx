import React from "react";
import {useState} from "react";
import "./Envir.css";
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
      <h1>Envirnoment</h1>
      <h3>Input an envirnoment into the simulation</h3>
      <h2>Temperature</h2>
      <h2>Percipitation</h2>

      <form onSubmit={handleSubmit}>
        <div id = "Month1">
            <label> Month 1:
            <input 
            type="text"
            name = "temp1"
            value = {inputs.temp1 || ""}
            onChange = {handleChange}
            />
            <input 
            type="text"
            name = "percip1"
            value = {inputs.percip1 || ""}
            onChange = {handleChange}
            />
            </label>
        </div>
            
        <div id = "Month 2">
            <label> Month 2;
            <input 
            type="text"
            name = "temp2"
            value = {inputs.temp2 || ""}
            onChange = {handleChange}
            />
            <input
            type="text"
            name = "percip2"
            value = {inputs.percip2|| ""}
            onChange= {handleChange}
            />
            </label>
        </div>

        <div id = "Month 3">
            <label> Month 3;
            <input 
            type="text"
            name = "temp3"
            value = {inputs.temp3 || ""}
            onChange = {handleChange}
            />
            <input
            type="text"
            name = "percip3"
            value = {inputs.percip3|| ""}
            onChange= {handleChange}
            />
            </label>
        </div>

        <div id = "Month 4">
            <label> Month 4;
            <input 
            type="text"
            name = "temp4"
            value = {inputs.temp4 || ""}
            onChange = {handleChange}
            />
            <input
            type="text"
            name = "percip4"

            value = {inputs.percip4|| ""}
            onChange= {handleChange}
            />
            </label>
        </div>

        <div id = "Month 5">
            <label> Month 5;
            <input 
            type="text"
            name = "temp5"
            value = {inputs.temp5 || ""}
            onChange = {handleChange}
            />
            <input
            type="text"
            name = "percip5"
            value = {inputs.percip5|| ""}
            onChange= {handleChange}
            />
            </label>
        </div>

        <div id = "Month 6">
            <label> Month 6;
            <input 
            type="text"
            name = "temp6"
            value = {inputs.temp6 || ""}
            onChange = {handleChange}
            />
            <input
            type="text"
            name = "percip6"
            value = {inputs.percip6|| ""}
            onChange= {handleChange}
            />
            </label>
        </div>

        <div id = "Month 7">
            <label> Month 7;
            <input 
            type="text"
            name = "temp7"
            value = {inputs.temp7 || ""}
            onChange = {handleChange}
            />
            <input
            type="text"
            name = "percip7"
            value = {inputs.percip7|| ""}
            onChange= {handleChange}
            />
            </label>
        </div>

        <div id = "Month 8">
            <label> Month 8;
            <input 
            type="text"
            name = "temp8"
            value = {inputs.temp8 || ""}
            onChange = {handleChange}
            />
            <input
            type="text"
            name = "percip8"
            value = {inputs.percip8|| ""}
            onChange= {handleChange}
            />
            </label>
        </div>

        <div id = "Month 9">
            <label> Month 9;
            <input 
            type="text"
            name = "temp9"
            value = {inputs.temp9 || ""}
            onChange = {handleChange}
            />
            <input
            type="text"
            name = "percip9"
            value = {inputs.percip9|| ""}
            onChange= {handleChange}
            />
            </label>
        </div>

        <div id = "Month 10">
            <label> Month 10;
            <input 
            type="text"
            name = "temp10"
            value = {inputs.temp10 || ""}
            onChange = {handleChange}
            />
            <input
            type="text"
            name = "percip10"
            value = {inputs.percip10|| ""}
            onChange= {handleChange}
            />
            </label>
        </div>

        <div id = "Month 11">
            <label> Month 11;
            <input 
            type="text"
            name = "temp11"
            value = {inputs.temp11 || ""}
            onChange = {handleChange}
            />
            <input
            type="text"
            name = "percip11"
            value = {inputs.percip11|| ""}
            onChange= {handleChange}
            />
            </label>
        </div>

        <div id = "Month 12">
            <label> Month 12;
            <input 
            type="text"
            name = "temp12"
            value = {inputs.temp12 || ""}
            onChange = {handleChange}
            />
            <input
            type="text"
            name = "percip12"
            value = {inputs.percip12|| ""}
            onChange= {handleChange}
            />
            </label>
        </div>

        <input type="submit" />


      </form>

      
    </main>
  );
}

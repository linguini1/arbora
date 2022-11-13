import './App.css';

//Hooks
import { useState, useEffect } from 'react';

//Pages
import Home from "../src/pages/Home";
import Plant from "../src/pages/Plant"
import Envir from "../src/pages/Envir";


//Component
import {Routes, Route} from "react-router-dom";
import Navbar from "./components/nav/Navbar";
import PageLink from "./components/nav/PageLink";

function App() {
  // Unpack and distribute data
  var version = "X.X.X";
  var organization = "Arbora";
  // Current page
  const [currentPage, setCurrentPage] = useState("/"); // To Do: Have the current page link highlighted red

  return (
    <div id="App">
      <Navbar version= {version} org = {organization} >
        <PageLink to = "/">Home</PageLink>
        <PageLink to = "/plant">Plant</PageLink>
        <PageLink to = "/envir">Envirnoment</PageLink>
      </Navbar>

      <Routes>
        <Route path = "/" element = {<Home/>}/>
        <Route path = "/plant"element= {<Plant/>}/>
        <Route path = "/envir"element = {<Envir/>}/>
      </Routes>
    </div>
  );
}

export default App;

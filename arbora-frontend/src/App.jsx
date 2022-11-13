import "./App.css";

//Hooks

//Pages
import Home from "./pages/Home";
import Plant from "./pages/Plant";
import Envir from "./pages/Envir";

//Component
import { Routes, Route } from "react-router-dom";
import PageLink from "./components/nav/PageLink";
import Navbar from "./components/nav/Navbar";

//components

function App() {
  return (
    <div id="App">
      <Navbar>
        <PageLink to="/">Home</PageLink>
        <PageLink to = "/plant">Plant</PageLink>
        <PageLink to = "/envir">Envirnoment</PageLink>
      </Navbar>
      <Routes>
        <Route path="/" element={<Home />}></Route>
        <Route path="/plant" element={<Plant />}></Route>
        <Route path="/envir" element={<Envir />}></Route>


        
      </Routes>
    </div>
  );
}

export default App;

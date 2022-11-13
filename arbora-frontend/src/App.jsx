import "./App.css";

//Hooks

//Pages
import Home from "./pages/Home";

//Component
import { Routes, Route } from "react-router-dom";
import PageLink from "./components/nav/PageLink";
import Navbar from "./components/nav/Navbar";

function App() {
  return (
    <div id="App">
      <Navbar>
        <PageLink to="/">Home</PageLink>
      </Navbar>
      <Routes>
        <Route path="/" element={<Home />}></Route>
      </Routes>
    </div>
  );
}

export default App;

import React from "react";
import "./Home.css";

// Hooks
import { useEffect, useState } from "react";

export default function Home() {
  const [data, setData] = useState([]);
  const months = 400 * 12;
  const [month, setMonth] = useState(0);

  function start_sim() {
    fetch("http://localhost:8000/start", {
      method: "POST",
      headers: {
        Accept: "application/json",
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ environment: "pukaskwa" }),
    });
  }

  function increment() {
    fetch("http://localhost:8000/increment", {
      method: "POST",
      headers: {
        Accept: "application/json",
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ month: month % 12 }),
    })
      .then((response) => response.json())
      .then((raw_data) => setData(raw_data));
    setMonth((month) => month + 1);
  }

  useEffect(() => {}, [data]);

  return (
    <main id="home">
      <h1>Home</h1>
      <div id="buttons">
        <button onClick={start_sim}>Start</button>
        <button onClick={increment}>Increment</button>
      </div>
      <canvas id="forest"></canvas>
    </main>
  );
}

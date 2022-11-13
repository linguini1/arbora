import React from "react";
import "./Navbar.css";


export default function Navbar({ version, org, children }) {
  return (
    <nav>
      <div id="arbora-info">
        <div id="logo">
          <img
            src={require("../../assets/logo.svg")}
            alt="Arbora Logo"
          />
        </div>
        <div id="sub-info">
          <div>
            <h1 id="org">{org}</h1>
            <p id="version">{`v${version}`}</p>
          </div>
        </div>
      </div>
      <div id="nav-links">{children}</div>
    </nav>
  );
}
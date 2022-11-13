import React from "react";

export default function Navbar({ children }) {
  return (
    <nav className="my_nav">
      <h1>Arbora</h1>
      <div id="nav-links">{children}</div>
    </nav>
  );
}

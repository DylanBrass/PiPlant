// NavigationBar.js
import React from 'react';
import { Link } from 'react-router-dom';
import './NavigationBar.css'; // Import the CSS file

const NavigationBar = () => {
  return (
    <nav>
      <ul>
        <li>
          <Link to="/" className="app-name">
            PiPlant
          </Link>
        </li>
        <li>
          <Link to="/">Home</Link>
        </li>
        <li>
          <Link to="/login">Login</Link>
        </li>
        <li>
            <Link to="/chart">Chart</Link>
        </li>
      </ul>
    </nav>
  );
};

export default NavigationBar;

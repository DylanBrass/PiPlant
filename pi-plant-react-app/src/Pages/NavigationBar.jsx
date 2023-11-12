// NavigationBar.js
import React from 'react';
import { Link } from 'react-router-dom';
import logo from "./logo.png"
import './NavigationBar.css'; // Import the CSS file

const NavigationBar = () => {
  return (
    <nav>
      <ul>
        <li>
          <Link to="/" className="app-name">
          <img src={logo}  atl="logo"/>
          </Link>
        </li>
        <li>
          <Link to="/" style={{color:'white'}}>Home</Link>
          </li>
        <li>
          <Link to="/login" style={{color:'white'}}>Login</Link>
        </li>
        <li>
            <Link to="/chart" style={{color:'white'}}>Chart</Link>
        </li>
      </ul>
    </nav>
  );
};

export default NavigationBar;

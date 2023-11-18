// NavigationBar.js
import React from 'react';
import { Link } from 'react-router-dom';
import logo from "./logo.png"
import './NavigationBar.css';
import axios from "axios"; // Import the CSS file

const NavigationBar = () => {
  const logout = () => {
    axios.post('http://' + window.location.hostname + ':5000/logout')
      .then(function (response) {
        console.log(response);
      })
      .catch(function (error) {
        console.log(error);
      });
  }
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
        <li>
            <button className="logout-button" onClick={logout}>
              Logout
            </button>
        </li>
      </ul>
    </nav>
  );
};

export default NavigationBar;

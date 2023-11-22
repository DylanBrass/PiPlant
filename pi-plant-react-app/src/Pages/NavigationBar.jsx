// NavigationBar.js
import React, {useEffect, useState} from 'react';
import { Link } from 'react-router-dom';
import logo from "./logo.png"
import './NavigationBar.css';
import axios from "axios";
import {useAuth} from "../AuthProvider/AuthProvider";


const NavigationBar = () => {
    const auth = useAuth();
      const logoutPost = () => {
        axios.post('http://' + window.location.hostname + ':5000/logout')
          .then(function (response) {
            console.log(response);
            auth.logout()
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
          {auth.isAuthenticated &&
            <li>
              <Link to="/" style={{color:'white'}}>Home</Link>
            </li>
          }
          {!auth.isAuthenticated &&
              <>
                <li>
                  <Link to="/login" style={{color:'white'}}>Login</Link>
                </li>
                <li>
                    <Link to="/register" style={{color:'white'}}>Register</Link>
                </li>
              </>
        }
            {auth.isAuthenticated &&
                <>
                    <li>
                        <Link to="/chart" style={{color:'white'}}>Chart</Link>
                    </li>

                    <li>
                        <button style={{color:'white'}} className="logout-button" onClick={logoutPost}>
                          Logout
                        </button>
                    </li>
                </>
          }
      </ul>
    </nav>
  );
};

export default NavigationBar;

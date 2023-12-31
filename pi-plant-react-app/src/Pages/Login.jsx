import NavigationBar from "./NavigationBar";
import React, {useEffect, useState} from 'react';
import './Login.css'; // Import your CSS file for styling
import plant1 from './Plant1.jpg'
import axios from "axios";
import {useAuth} from "../AuthProvider/AuthProvider";

axios.defaults.withCredentials = true

function Login() {
    const auth = useAuth();

    const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  const handleEmailChange = (e) => {
    setUsername(e.target.value);
  }

  const handlePasswordChange = (e) => {
    setPassword(e.target.value)
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    // You can add your login logic here

    axios.post('http://' + window.location.hostname + ':5000/login', {
        username: username,
        password:  password
    })
        .then(function (response) {
            console.log(response);
          if (response.status === 200) {
              auth.login()
          }
        })
        .catch(function (error) {
          alert("Error logging in please try again" + error)
            console.log(error);

        });

  };


  return (
    <div>
      <NavigationBar />

      <div className="login-container">
      <img src={plant1} alt="Plant" className="login-box-image"/>
      
        <div className="login-box" style={{ height: '60%' }}>
          <h1 className="login-title">Login</h1>
          <form onSubmit={handleSubmit}>
            <div className="form-group">
              <label htmlFor="email">Email</label>
              <input
                id="username"
                value={username}
                onChange={handleEmailChange}
              />
            </div>
            <div className="form-group">
              <label htmlFor="password">Password</label>
              <input
                type="password"
                id="password"
                value={password}
                onChange={handlePasswordChange}
              />
            </div>
            <button className="login-button" type="submit">Login</button>
          </form>
            <a href="/register" className="register-link">Register</a>
        </div>
      </div>
    </div>
  );
}

export default Login;

import NavigationBar from "./NavigationBar";
import React, { useState } from 'react';
import './Login.css'; // Import your CSS file for styling

function Login() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const handleEmailChange = (e) => {
    setEmail(e.target.value);
  };

  const handlePasswordChange = (e) => {
    setPassword(e.target.value);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    // You can add your login logic here
  };

  return (
    <div>
      <NavigationBar />
      <div className="login-container">
        <div className="login-box">
          <h1 className="login-title">Login</h1>
          <form onSubmit={handleSubmit}>
            <div className="form-group">
              <label htmlFor="email">Email:</label>
              <input
                type="email"
                id="email"
                value={email}
                onChange={handleEmailChange}
              />
            </div>
            <div className="form-group">
              <label htmlFor="password">Password:</label>
              <input
                type="password"
                id="password"
                value={password}
                onChange={handlePasswordChange}
              />
            </div>
            <button className="login-button" type="submit">Login</button>
          </form>
        </div>
      </div>
    </div>
  );
}

export default Login;

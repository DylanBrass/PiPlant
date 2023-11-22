import React from 'react';
import axios from "axios";
import {redirect} from "react-router-dom";
import NavigationBar from './NavigationBar';
import './RegisterPage.css';
import plant1 from './Plant1.jpg'

function RegisterPage() {
    const register = (event) => {
        event.preventDefault();
        console.log("Registering...");
        axios.post('http://' + window.location.hostname + ':5000/register', {
            username: event.target[0].value,
            password: event.target[1].value
        }).then(function (response) {
            console.log(response);
            window.location.href = "/login"
        }).catch(function (error) {
            console.log(error);
        })
    }
    return (
        <div>
            <NavigationBar />
            <div className="register-container">
                <img src={plant1} alt="Plant" className="login-box-image"/>

                <div className="register-box"  style={{ height: '60%' }}>
                    <h1 className="register-title">Register</h1>
                    <form onSubmit={register}>
                        <div className="form-group">
                            <label htmlFor="email">Email</label>
                            <input id="username" />
                        </div>
                        <div className="form-group">
                            <label htmlFor="password">Password</label>
                            <input type="password" id="password" />
                        </div>
                        <button className="register-button" type="submit">Register</button>
                    </form>
                </div>
            </div>
        </div>
    );
}

export default RegisterPage;
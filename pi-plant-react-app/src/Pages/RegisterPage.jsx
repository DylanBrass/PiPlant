import React from 'react';
import axios from "axios";
import {redirect} from "react-router-dom";

function RegisterPage() {
    const register = (event) => {
        event.preventDefault();
        console.log("Registering...");
        axios.post('http://' + window.location.hostname + ':5000/register', {
            username: event.target[0].value,
            password: event.target[1].value
        }).then(function (response) {
            console.log(response);
            alert("Registered!")
            redirect("/login")
        }).catch(function (error) {
            console.log(error);
        })
    }
    return (
        <div>
            <h1>Register Page</h1>
            <form onSubmit={register}>
                <input type="text" placeholder="Username" />
                <input type="password" placeholder="Password" />
                <button type="submit">Register</button>
            </form>
        </div>
    );
}

export default RegisterPage;
import Navbar from "./NavigationBar";
import './HomePage.css';
import axios from 'axios'
import { useState } from "react";





function MainPage() {
  const[recentValues, setRecentValues] = useState("No recent values")
  const[lightStatus, setLightStatus] = useState("Light status is unknown")
  const getRecent = () =>{
    axios
          .get('http://'+window.location.hostname+':5000/getCurrentValue')
          .then(function (response) {
            setRecentValues(response.data.currentValue)
          })
          .catch((error) => {
            console.log(error);
        })
  }

  const toggleLight = () =>{
    axios.post('http://'+window.location.hostname+':5000/toggleLight/1')
    .then(function (response) {
      setLightStatus(response.data.lightStatus)
    })
    .catch(function (error) {
      console.log(error);
    });
  }
  return (
    <div>
      <Navbar />
      <h1>Home Page</h1>
      <button onClick={()=>{
        toggleLight()
      }}>Toggle Light</button>
      <p>This is the home page.</p>
      <button onClick={()=> getRecent()}>Get Current Value</button>

      <h2>Recent Values</h2>
      <p>{recentValues}</p>
    </div>
  );
}

export default MainPage;
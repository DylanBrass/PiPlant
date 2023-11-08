import Navbar from "./NavigationBar";
import './HomePage.css';
import axios from 'axios'
import { useState } from "react";





function MainPage() {
  const[recentValues, setRecentValues] = useState("No recent values")
  const[lightStatus, setLightStatus] = useState("Light status is unknown")
  const[selectedLight, setSelectedLight] = useState(1)
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
    axios.post('http://'+window.location.hostname+':5000/toggleLight/' + selectedLight)
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
      <select
        onChange={(e) => selectedLight(e.target.value)}
        defaultValue={setSelectedLight}
      >
        {
          axios.get('http://'+window.location.hostname+':5000/numberOfLights')
          .then(function (response) {
            for (let i = 1; i <= response.data.numberOfLights; i++) {
              return <option value={i}>{i}</option>
            }
          }.catch(function (error) {
            console.log(error);
          }))

        }
          
      </select>
      <button onClick={()=>{
        toggleLight()
      }}>Toggle Light</button>
      <h2>Light Status</h2>
      <p>{lightStatus}</p>


      <p>This is the home page.</p>
      <button onClick={()=> getRecent()}>Get Current Value</button>

      <h2>Recent Values</h2>
      <p>{recentValues}</p>
    </div>
  );
}

export default MainPage;
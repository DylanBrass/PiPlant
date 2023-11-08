import Navbar from "./NavigationBar";
import './HomePage.css';
import axios from 'axios'
import { useState } from "react";
import { useEffect } from "react";





function MainPage() {
  const[recentValues, setRecentValues] = useState({allValues: []})
  const[selectedLight, setSelectedLight] = useState(1)
  const[numberOfLights, setNumberOfLights] = useState(0)
  const getRecent = () =>{
    axios
          .get('http://'+window.location.hostname+':5000/getCurrentValue')
          .then(function (response) {
            console.log(response.data)
            console.log(response)
            setRecentValues(response.data.allValues)
          })
          .catch((error) => {
            console.log(error);
        })
  }

  const toggleLight = () =>{
    axios.post('http://'+window.location.hostname+':5000/toggleLight/' + selectedLight)
    .then(function (response) {
      console.log(response)
      alert("Light is now " + response.data.lightStatus)
    })
    .catch(function (error) {
      console.log(error)
    });

    
  }
  useEffect(() => {
    axios.get('http://'+window.location.hostname+':5000/numberOfLights')
    .then(function (response) {
      setNumberOfLights(response.data.numberOfLights)
    }).catch(function (error) {
      console.log(error);
    })
  },[]) 
  return (
    <div>
      <Navbar />
      <h1>Home Page</h1>
      <select
        onChange={(e) => setSelectedLight(e.target.value)}
        defaultValue={selectedLight}
      >
        {
          Array.from(Array(numberOfLights).keys()).map((i) => {
            return <option value={i+1}>{i+1}</option>
          })
        }         
      </select>
      <button onClick={()=>{
        toggleLight()
      }}>Toggle Light</button>


      <p>This is the home page.</p>
      <button onClick={()=> getRecent()}>Get Current Value</button>

      <h2>Recent Values</h2>
      {
        recentValues.map((value, index)=>{
          return <p id={index} >{value}</p>
        })
      }
    </div>
  );
}

export default MainPage;
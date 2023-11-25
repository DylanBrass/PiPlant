import Navbar from "./NavigationBar";
import './HomePage.css';
import axios from 'axios';
import { useState, useEffect } from "react";
import plant2 from './Plant2.png';
import gradientBackground from './gradientBackground.avif';
import lightBulb2 from './light-bulb.png';
import lightBulb1 from './light-bulb2.png';
import 'bootstrap/dist/css/bootstrap.min.css';
import { useAuth } from "../AuthProvider/AuthProvider";

axios.defaults.withCredentials = true
function MainPage() {
  const auth = useAuth();

  const [recentValues, setRecentValues] = useState([]);
  const [selectedLight, setSelectedLight] = useState(1);
  const [numberOfLights, setNumberOfLights] = useState(0);
  const [isLightOn, setIsLightOn] = useState(false);

  const getRecent = () => {
    axios
      .get('http://' + window.location.hostname + ':5000/getCurrentValues')
      .then(function (response) {
        setRecentValues(response.data.allValues);
        console.log(response.data.allValues)
      })
      .catch((error) => {
        console.log(error);
        if (error.response.status === 401) {
          auth.authError()
        }
      });
  };

  const toggleLight = () => {
    axios.post('http://' + window.location.hostname + ':5000/toggleLight/' + selectedLight)
      .then(function (response) {
        console.log(response);
        const newLightStatus = response.data.lightStatus;
        setIsLightOn(newLightStatus);
      })
      .catch(function (error) {
        console.log(error);
        if (error.response.status === 401) {
          auth.authError()
        }
      });
  };

  const isLightToggled = () => {
    axios.get('http://' + window.location.hostname + ':5000/lightStatus/' + selectedLight)
      .then(function (response) {
        console.log(response);
        const lightStatus = response.data.lightStatus
        setIsLightOn(lightStatus)
      })
      .catch(function (error) {
        console.log(error);
        if (error.response.status === 401) {
          auth.authError();
        }
      });
  };
  

  useEffect(() => {
    if (!auth.isAuthenticated) {
      window.location.href = "/login"
    }
    axios.get('http://' + window.location.hostname + ':5000/numberOfLights')
      .then(function (response) {
        console.log(response.data.numberOfLights);
        setNumberOfLights(response.data.numberOfLights);
      }).catch(function (error) {
        console.log(error);
      });
    // isLightToggled()
    getRecent();
  }, []);

  useEffect(() => {
    isLightToggled()
  }, [selectedLight])

  return (

    <div>
      <Navbar />

      <div className="container">

        <h1>My Plant Health</h1>
        <div className="box">
          <div className="row">
            <div className="col">
              <h2>Lights</h2>
              <p>Please select the light you wish to toggle</p>
              <div className="col-hor">
                <select
                  onChange={(e) => setSelectedLight(e.target.value)}
                  defaultValue={selectedLight}>
                  {Array.from(Array(numberOfLights).keys()).map((i) => (
                    <option value={i + 1} key={i + 1}>{i + 1}</option>
                  ))}
                </select>
                <button className="toggle-button" onClick={() => toggleLight()}>
                  <img src={isLightOn ? lightBulb2 : lightBulb1} alt="Lightbulb Image" className="toggle-img" />
                </button>
              </div>
            </div>
            <div className="col">
              <h2>Plant Statistics</h2>
              <p>Press to generate current plant values</p>
              <button className="button" role="button" onClick={() => getRecent()}>Get Current Value</button>
              {recentValues.map(element => (
                <div key={element.sensorNum}>
                  <hr/>
                  <h3>Plant #{element.sensorNum}</h3>
                  <p>Value: {element.values.Value}</p>
                  <p>Voltage: {element.values.Voltage}</p>
                </div>
              ))}
            </div>
            <div className="col">
              <img src={plant2} alt="Plant Image" className="img" />
            </div>
          </div>
        </div>
      </div>
    </div>


  );
}

export default MainPage;

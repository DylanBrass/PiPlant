import axios from 'axios';
import './ChartPage.css';
import React, { useEffect, useState } from 'react'
import { LineChart, Line, CartesianGrid, XAxis, YAxis } from 'recharts';
import Navbar from './NavigationBar';
import DatePicker from "react-datepicker";
import 'react-datepicker/dist/react-datepicker.css'
import { useAuth } from "../AuthProvider/AuthProvider";

axios.defaults.withCredentials = true

function ChartPage() {
    const auth = useAuth();

    const [data, setData] = useState([])

    const [selectedDate, setSelectedDate] = useState(new Date());

    const [selectedSensor, setSelectedSensor] = useState(1);

    const [numberOfSensors, setNumberOfSensors] = useState(2);

    const numberOfSensorsFunc = () => {
        axios.get('http://' + window.location.hostname + ':5000/numberOfMoistureSensors')
            .then(function (response) {
                console.log(response.data.numberOfSensors)
                setNumberOfSensors(response.data.numberOfSensors)
            })
            .catch(function (error) {
                console.log(error)

                if (error.response.status === 401) {
                    auth.authError()
                }
            })
    }

    const fetchData = () => {
        axios.get('http://' + window.location.hostname + ':5000/getValuesForDay/' + selectedDate.toLocaleDateString('fr-CA').replaceAll('/', '-') + '/' + selectedSensor)
            .then(function (response) {
                console.log(response.data.values)
                setData(response.data.values)
            })
            .catch(function (error) {
                console.log(error)
                setData([])
                if (error.response.status === 404) {
                    alert("No data for this date")
                }

                if (error.response.status === 401) {
                    auth.authError()
                }
            })
    }
    useEffect(() => {
        numberOfSensorsFunc()
        fetchData()
    }, []);

    useEffect(() => {
        fetchData()
    }, [selectedDate, selectedSensor])


    return (
        <div>
            <Navbar />
            <center>
                <h1>Chart Page</h1>

                <div className='box'>
                    <div className='chart'>
                        <LineChart width={700} height={500} data={data}>
                            <XAxis tick={{ color: "#000000" }} dataKey="time" />
                            <YAxis tick={{ color: "#000000" }} dataKey="value" type="number" domain={[0, 'dataMax']} />
                            <CartesianGrid stroke="#000000" strokeDasharray="5 5" fill='white' />
                            <Line type="monotone" dataKey="value" stroke="#000000" />
                        </LineChart>
                    </div>
                    <br />
                    <div className='datepicker'>
                        <DatePicker
                            showIcon
                            dateFormat="yyyy-MM-dd"
                            selected={selectedDate}
                            onChange={(date) => setSelectedDate(date)}
                        />
                        <select
                            onChange={(e) => setSelectedSensor(e.target.value)}
                            defaultValue={selectedSensor}>
                            {Array.from(Array(numberOfSensors).keys()).map((i) => (
                                <option value={i + 1} key={i + 1}>{i + 1}</option>
                            ))}
                        </select>
                    </div>
                </div>
            </center>
        </div>
    )
}

export default ChartPage
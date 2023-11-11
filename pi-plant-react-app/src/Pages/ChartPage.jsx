import axios from 'axios';
import React, { useEffect, useState } from 'react'
import { LineChart, Line, CartesianGrid, XAxis, YAxis } from 'recharts';
import Navbar from './NavigationBar';
import DatePicker from "react-datepicker";
import 'react-datepicker/dist/react-datepicker.css'

function ChartPage() {

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
            alert("No data for this date")
        })
    }
    useEffect(() => {
        numberOfSensorsFunc()

        fetchData()
    },[]);

    useEffect(() => {
        fetchData()
    }, [selectedDate, selectedSensor])


    return (
        <div>
            <Navbar />
            <h1>Chart Page</h1>
            
            
            <LineChart width={500} height={300} data={data}>
                <XAxis dataKey="time" />
                <YAxis dataKey="value" />
                <CartesianGrid stroke="#eee" strokeDasharray="5 5" />
                <Line type="monotone" dataKey="value" stroke="#82ca9d" />
            </LineChart>

            <br/>
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
    )
}

export default ChartPage
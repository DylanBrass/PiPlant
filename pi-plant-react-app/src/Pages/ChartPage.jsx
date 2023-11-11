import axios from 'axios';
import React, { useEffect, useState } from 'react'
import { LineChart, Line, CartesianGrid, XAxis, YAxis } from 'recharts';
import Navbar from './NavigationBar';
import DatePicker from "react-datepicker";

function ChartPage() {

    const [data, setData] = useState([])

    const [selectedDate, setSelectedDate] = useState(new Date().toLocaleDateString('fr-CA').replaceAll('/', '-'));

    const [selectedSensor, setSelectedSensor] = useState(1);

    const numberOfSensors = () => {
        axios.get('http://' + window.location.hostname + ':5000/numberOfMoistureSensors')
        .then(function (response) {
            console.log(response.data.numberOfSensors)
            return response.data.numberOfSensors
        })
        .catch(function (error) {
            console.log(error)
        })
    }

    const fetchData = () => {
        axios.get('http://' + window.location.hostname + ':5000/getValuesForDay/' + selectedDate + '/' + selectedSensor)
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
        fetchData()
        numberOfSensors()
    },[]);


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
            <DatePicker
                wrapperClassName="datePicker"
                dateFormat="yyyy-MM-dd"
                selected={new Date()}
                onChange={(date) => setSelectedDate(date.toLocaleDateString('fr-CA'))}
                // Add styles to the DatePicker
                style={{ marginTop: '10px', marginBottom: '10px', width: '100%' }}
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
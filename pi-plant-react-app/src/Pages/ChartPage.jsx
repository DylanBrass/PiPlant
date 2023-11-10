import axios from 'axios';
import React, { useEffect, useState } from 'react'
import { LineChart, Line, CartesianGrid, XAxis, YAxis } from 'recharts';



function ChartPage() {

    const [data, setData] = useState([])

    const fetchData = () => {
        axios.get('http://' + window.location.hostname + ':5000/getValuesForDay/2023-11-10/1')
        .then(function (response) {
            console.log(response.data.values)
            setData(response.data.values)
        })
        .catch(function (error) {
            console.log(error)
        })
    }
    useEffect(() => {
        fetchData()
    },[]);


    return (
        <div>
            <LineChart width={500} height={300} data={data}>
                <XAxis dataKey="time" />
                <YAxis dataKey="value" />
                <CartesianGrid stroke="#eee" strokeDasharray="5 5" />
                <Line type="monotone" dataKey="value" stroke="#82ca9d" />
            </LineChart>
        </div>
    )
}

export default ChartPage
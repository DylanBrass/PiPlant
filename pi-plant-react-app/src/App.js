import React from 'react';
import HomePage from './Pages/HomePage';
import Login from './Pages/Login';
import ChartPage from './Pages/ChartPage';
import {
  BrowserRouter,
  Routes, // instead of "Switch"
  Route,
} from "react-router-dom";
import RegisterPage from "./Pages/RegisterPage";

const App = () => {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/login" element={<Login />} />
        <Route path="/chart" element={<ChartPage/>} />
        <Route path="/register" element={<RegisterPage/>} />
        <Route path="*" element={<h1>Not Found</h1>} />
      </Routes>
    </BrowserRouter>
  );
};

export default App;

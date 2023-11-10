import React from 'react';
import HomePage from './Pages/HomePage';
import Login from './Pages/Login';
import {
  BrowserRouter,
  Routes, // instead of "Switch"
  Route,
} from "react-router-dom";
import ChartPage from './Pages/ChartPage';

const App = () => {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/login" element={<Login />} />
        <Route path="/chart" element={<ChartPage/>} />
      </Routes>
    </BrowserRouter>
  );
};

export default App;

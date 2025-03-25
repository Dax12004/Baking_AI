import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Navbar from './components/Navbar';
import HomePage from './pages/HomePage';
import RecipesPage from './pages/RecipesPage';
import ContactPage from './pages/AboutPage';
import 'bootstrap/dist/css/bootstrap.min.css';
import './App.css';

const App = () => {
  return (
    <>
      <Router>
        <Navbar />
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="/recipes" element={<RecipesPage />} />
          <Route path="/contact" element={<ContactPage />} />
        </Routes>
      </Router>

    </>
  );
};

export default App;
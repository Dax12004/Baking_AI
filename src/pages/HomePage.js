import React from 'react';
import { useNavigate } from 'react-router-dom';
import 'bootstrap/dist/css/bootstrap.min.css';
import './Homepage.css';

function Homepage() {
  const navigate = useNavigate();

  const handleGetStarted = () => {
    navigate('/recipes');
  };

  return (
    <div className="homepage-container d-flex justify-content-center align-items-center">
      <div className="container text-center p-5">
        {/* Set all text to yellow by applying 'animated-text' class */}
        <h1 className="homepage-heading animated-text">
          Generate Delicious Recipes with Your Ingredients
        </h1>
        <p className="lead animated-text mb-4">
          Simply input your available ingredients, select dietary preferences, and let our AI create unique and delicious recipes just for you.
        </p>
        <button 
          onClick={handleGetStarted} 
          className="btn btn-primary btn-lg animated-btn"
        >
          Get Started
        </button>
      </div>
    </div>
  );
}

export default Homepage;

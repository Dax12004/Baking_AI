import React from 'react';
import { useNavigate } from 'react-router-dom';  // Import for navigation
import './Navbar.css';

const Navbar = () => {
    const navigate = useNavigate();  // Hook for routing

    return (
        <nav className="navbar">
            <div className="navbar-title" onClick={() => navigate('/')}>
                Baking AI
            </div>
            <div className="navbar-buttons">
                <button className="nav-btn" onClick={() => navigate('/recipes')}>
                    Discover Recipes
                </button>&nbsp;&nbsp;&nbsp;&nbsp;
                <button className="nav-btn" onClick={() => navigate('/contact')}>
                    Contact Us
                </button>
            </div>
        </nav>
    );
};

export default Navbar;

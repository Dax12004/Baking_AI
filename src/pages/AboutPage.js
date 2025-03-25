// AboutPage.js
import React, { useEffect } from 'react';
import './AboutPage.css';
import teamImage from '../Assets/team_member.jpg';

const About = () => {
    // Function to trigger the scroll animations
    const handleScroll = () => {
        const scrollElements = document.querySelectorAll('.fade-in-scroll');

        scrollElements.forEach(element => {
            const rect = element.getBoundingClientRect();
            if (rect.top < window.innerHeight && rect.bottom >= 0) {
                element.classList.add('visible');
            } else {
                element.classList.remove('visible');
            }
        });
    };

    useEffect(() => {
        window.addEventListener('scroll', handleScroll);
        handleScroll(); // Run on page load
        return () => window.removeEventListener('scroll', handleScroll); // Clean up event listener
    }, []);

    return (
        <div className="about-container">
            <div className="intro-section fade-in-scroll">
                <div className="left-image">
                    <img src={teamImage} alt="Team" />
                </div>
                <div className="description">
                    <h1>About Our Website</h1>
                    <p className='about-para'>
                        Our Baking AI website is meant to make and enhance your baking simpler. Other recipe websites show ingredient quantities in spoons or cups, but our website provides the precise gram quantities of all ingredients. This helps you with greater accuracy, consistency, and better results in your baking. If you are a beginner experimenting with new recipes or a professional baker looking for perfection, our tool saves you from guesswork and ensures perfect texture, flavor, and presentation. With our easy interface and intelligent AI-based conversion system, baking has never been simpler or more accurate.
                    </p>
                </div>
            </div>

            <h1 className="fade-in-scroll">About Our Team</h1>
            <p className="fade-in-scroll">
                We are a passionate team dedicated to building innovative solutions. Our team specializes in frontend
                and backend development, with expertise in React, JavaScript, and Python.
            </p>
            <div className="team-section">
                <div className="team-member fade-in-scroll">
                    <h2>Parmar Daksh</h2>
                    <p>Role: Team Leader & Backend Developer</p>
                    <p>Skills: Python, API Development, Baking AI Integration</p>
                </div>
                <div className="team-member fade-in-scroll">
                    <h2>Harshit Bhalani</h2>
                    <p>Role: Frontend Developer</p>
                    <p>Skills: JavaScript, React, UI/UX Design</p>
                </div>
                <div className="team-member fade-in-scroll">
                    <h2>Bhavsar Daksh</h2>
                    <p>Role: Frontend Developer & DevOps Engineer</p>
                    <p>Skills: React, JavaScript, Docker, AWS, CI/CD Pipelines</p>
                </div>
            </div>
            <div className="tech-stack fade-in-scroll">
                <h2>Technology Stack</h2>
                <p>Frontend: React, JavaScript</p>
                <p>Backend: Python</p>
            </div>
        </div>
    );
};

export default About;

import React from 'react';
import { useNavigate } from "react-router";
import '../styles/WelcomePage.css';

const WelcomePage = () => {
  const navigate = useNavigate();

  const handleSignIn = () => {
    console.log("button clicked")
    navigate ("/signin");
  };

  return (
    <div className="welcome-container">
      <nav className="navbar">
        <div className="logo">
          <img src="./Components/images/logo.png"alt="Church Logo" />
        </div>
        <div className="nav-buttons">
          <button className="nav-btn" onClick={handleSignIn} type='button'>SignIn</button>
        </div>
      </nav>

      <main className="main-content">
        <div className="welcome-box">
          <h1 className="welcome-text">WELCOME TO</h1>
          <h2 className="church-name">CHURCH NAME HERE</h2>
          <p className="subtitle">Where the glory dwells in our hearts daily</p>
        </div>
      </main>
    </div>
  );
};

export default WelcomePage;
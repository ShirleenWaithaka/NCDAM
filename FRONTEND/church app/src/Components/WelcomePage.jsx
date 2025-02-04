import React from "react";
import { Link } from "react-router-dom";
import "../styles/WelcomePage.css";

import logo from "../Components/images/NCDAM.png";

const WelcomePage = () => {
  return (
    <div className="body">
      <nav className="navbar">
        <div className="logo">
          <img src={logo} alt="Church Logo" />
        </div>
        <div className="nav-buttons">
          <Link to="/signup" className="signup-btn">SIGN UP</Link>
          <Link to="/signin" className="signin-btn">SIGN IN</Link>
          <Link to="/pastors" className="pastors-btn">OUR PASTORS</Link>
          <Link to="/services" className="services-btn">OUR SERVICES</Link>
          
        </div>
      </nav>
      
      <main className="main-content">
        <div className="welcome-box">
          <h1 className="welcome-text">WELCOME TO</h1>
          <h1 className="church-name">NAIROBI CHAPEL DAM</h1>
          <p className="subtitle">Where the glory dwells in our hearts daily</p>
        </div>
      </main>
    </div>
  );
};

export default WelcomePage;

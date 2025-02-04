import React, { useState } from 'react';
import '../styles/SignIn.css';

const SignIn = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    // Add your sign in logic here
    console.log('Sign in attempted with:',{ email, password});
  };

  return (
    <div className="page-background">
      <div className="signin-container">
        <div className="signin-box">
          <h1>SIGN IN</h1>
          <form onSubmit={handleSubmit}>
            <div className="input-group">
              <input
                type="email"
                placeholder="Email Address"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                required
              />
            </div>
            <div className="input-group">
              <input
                type="password"
                placeholder="Password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                required
              />
            </div>
            <button type="submit" className="signin-btn">Sign In</button>
          </form>
        </div>
      </div>
    </div>
  );
};

export default SignIn;
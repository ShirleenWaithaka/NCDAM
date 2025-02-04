import React from 'react';
import { BrowserRouter,Routes, Route } from 'react-router-dom';
import WelcomePage from "./Components/WelcomePage";
import SignIn from "./Components/SignIn";
import SignUp from "./Components/SignUp";
import Pastors from "./Components/Pastors";
import Services from "./Components/Services";
const App = () => {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={ <WelcomePage />} />
        <Route path="/signin" element={ <SignIn />} />
        <Route path="/signup" element={<SignUp />} />
        <Route path="/pastors" element={<Pastors />} />
        <Route path="/services" element={<Services />} />
      </Routes>
    </BrowserRouter>
  );
};

export default App;
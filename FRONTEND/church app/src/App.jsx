import React from 'react';
import { BrowserRouter,Routes, Route } from 'react-router-dom';
import WelcomePage from "./Components/WelcomePage";
import SignIn from "./Components/SignIn";

const App = () => {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={ <WelcomePage />} />
        <Route path="/signin" element={ <SignIn />} />
      </Routes>
    </BrowserRouter>
  );
};

export default App;
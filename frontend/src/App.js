import React from "react";

import { BrowserRouter as Router, Routes, Route } from "react-router-dom";

import Home from "./components/Home/Home";
import "./App.css";

class App extends React.Component {
  render() {
    return (
      <Router>
        <Routes>
          <Route exact path="/" element={<Home />}></Route>
        </Routes>
      </Router>
    );
  }
}

export default App;

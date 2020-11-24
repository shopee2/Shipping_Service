import logo from "./logo.svg";
import "./App.css";
import { Component } from "react";
import { BrowserRouter, Route, Link, Router, Redirect } from "react-router-dom";
import Home from "./Components/Home";
import Dashboard from "./Components/Dashboard";
class App extends Component {
  render() {
    return (
      <div>
        <div>
          <Route exact path="/home" component={Home}></Route>
          <Route exact path="/" component={Dashboard}></Route>
        </div>
      </div>
    );
  }
}

export default App;

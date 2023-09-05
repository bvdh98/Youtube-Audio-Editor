import logo from "./logo.svg";
import "./App.css";
import "bootstrap/dist/css/bootstrap.min.css";
import Button from "react-bootstrap/Button";
import { useEffect, useState } from "react";

//todo: disable download button until download finished
const endpoint = "http://localhost:5000/api/video";

const App = () => {
  const [data, setData] = useState();
  const download = async () => {
    const res = await fetch(endpoint, {
      method: "POST",
      mode: "no-cors",
      headers: { "Content-Type": "application/json" },
    });
    // const status = await res.json()
    setData(res);
    console.log(res);
  };
  return (
    <div className="App">
      <Button onClick={download}>download</Button>
    </div>
  );
};

export default App;

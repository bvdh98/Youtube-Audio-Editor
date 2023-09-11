import "./App.css";
import "bootstrap/dist/css/bootstrap.min.css";
import Button from "react-bootstrap/Button";
import { useEffect, useState } from "react";
import Video from "./Components/Video";

//todo: disable download button until download finished
const endpoint = "http://localhost:5000/api/video";

const App = () => {
  const [status, setStatus] = useState();
  const download = async () => {
    const res = await fetch(endpoint, {
      method: "POST",
      mode: "cors",
      headers: { "Content-Type": "application/json" }
    });
    // const status = await res.json()
    setStatus(res.status);
    console.log(status)
  };
  return (
    <div className="App">
      <Button onClick={download}>download</Button>
      {status === 200 ? <Video></Video>:null}
    </div>
  );
};

export default App;


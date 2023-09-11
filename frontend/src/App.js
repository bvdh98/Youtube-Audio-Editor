import "./App.css";
import "bootstrap/dist/css/bootstrap.min.css";
import Button from "react-bootstrap/Button";
import { useEffect, useState } from "react";
import Video from "./Components/Video";

//todo: disable download button until download finished
const endpoint = "http://localhost:5000/api/video";

const App = () => {
  const [status, setStatus] = useState();
  const [downloadDisabled, setDownloadDisabled] = useState(false)
  const download = async () => {
    setDownloadDisabled(true)
    const res = await fetch(endpoint, {
      method: "POST",
      mode: "cors",
      headers: { "Content-Type": "application/json" }
    });
    setStatus(res.status);
    setDownloadDisabled(false)
  };
  return (
    <div className="App">
      <Button onClick={download} disabled={downloadDisabled}>download</Button>
      {status === 200 ? <Video></Video>:null}
    </div>
  );
};

export default App;


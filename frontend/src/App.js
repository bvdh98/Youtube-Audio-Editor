import "./App.css";
import "bootstrap/dist/css/bootstrap.min.css";
import { Suspense, useState } from "react";
import Video from "./Components/Video";
import DownloadButton from "./Components/DownloadButton";
//TODO:handle errors when video download fails
//TODO:show loading during download

const App = () => {
  const [status, setStatus] = useState(null);
  return (
    <div className="App">
      <DownloadButton setStatus={setStatus}></DownloadButton>
      <Video status={status}></Video>
    </div>
  );
};
export default App;

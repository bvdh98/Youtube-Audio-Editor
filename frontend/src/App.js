import "./App.css";
import "bootstrap/dist/css/bootstrap.min.css";
import { createContext, useState, useEffect } from "react";
import Video from "./Components/Video";
import SearchForm from "./Components/SearchForm";
import Row from "react-bootstrap/Row";
//TODO:handle errors when video download fails
//TODO:clear form after submit
//TODO:disable cra error screen
//TODO:downloading state doesnt persist between refreshes
export const statusContext = createContext(null);
const App = () => {
  const [status, setStatus] = useState(null);
  useEffect(() => {
    getData();
  }, []);
  const getData = async () => {
    const res = await fetch('http://localhost:5000/api/downloadstatus',{credentials: 'include'})
    const data = await res.json()
    if (data.isDownloading) {
      setStatus("downloading")
    }
  }
  return (
    <div className="App">
      <statusContext.Provider value={{ status, setStatus }}>
        <Row>
          <div className="col-sm-8" id="content">
            <SearchForm />
            <Video />
          </div>
        </Row>
      </statusContext.Provider>
    </div>
  );
};
export default App;

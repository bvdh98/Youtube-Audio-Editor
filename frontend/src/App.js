import "./App.css";
import "bootstrap/dist/css/bootstrap.min.css";
import { createContext, useState } from "react";
import Video from "./Components/Video";
import SearchForm from "./Components/SearchForm";
//TODO:handle errors when video download fails
//TODO:clear form after submit
//TODO:prevent null input
//TODO:disable cra error screen
//TODO:video not playable error
export const statusContext = createContext(null);
const App = () => {
  const [status, setStatus] = useState(null);
  return (
    <div className="App">
      <statusContext.Provider value={{status,setStatus}}>
        <SearchForm />
        <Video/>
      </statusContext.Provider>
    </div>
  );
};
export default App;

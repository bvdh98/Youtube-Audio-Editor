import React, { useContext } from "react";
import { useState } from "react";
import Button from "react-bootstrap/Button";
import { statusContext } from "../App";
const endpoint = "http://localhost:5000/api/video";

const SubmitButton = ({audioLink,vidLink}) => {
  const {setStatus} = useContext(statusContext)
  const [downloadDisabled, setDownloadDisabled] = useState(false);
  const download = async () => {
    setStatus("downloading");
    setDownloadDisabled(true);
    const res = await fetch(endpoint, {
      method: "POST",
      mode: "cors",
      headers: { "Content-Type": "application/json" },
      body:JSON.stringify({'audioLink':audioLink,'vidLink':vidLink})
    });
    const resMessage = await res.json()
    setStatus(resMessage.message);
    setDownloadDisabled(false);
  };
  return (
    <Button onClick={download} disabled={downloadDisabled}>
      Submit
    </Button>
  );
};

export default SubmitButton;

import React, { useContext } from "react";
import { useState } from "react";
import Button from "react-bootstrap/Button";
import { statusContext } from "../App";
const endpoint = "http://localhost:5000/api/video";

const SubmitButton = ({ form, setErrors, findFormErrors }) => {
  const { setStatus } = useContext(statusContext)
  const [downloadDisabled, setDownloadDisabled] = useState(false);
  const download = async () => {
    setStatus("downloading");
    setDownloadDisabled(true);
    const res = await fetch(endpoint, {
      method: "POST",
      mode: "cors",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ 'audioLink': form.audioLink, 'vidLink': form.videoLink })
    });
    const resMessage = await res.json()
    setStatus(resMessage.message);
    setDownloadDisabled(false);
  };
  const handleSubmit = (e) => {
    e.preventDefault();
    // get errors
    const newErrors = findFormErrors();
    // check for errors
    if (Object.keys(newErrors).length > 0) {
      setErrors(newErrors);
    } else {
      download()
    }
  }
  return (
    <Button onClick={handleSubmit} disabled={downloadDisabled}>
      Submit
    </Button>
  );
};

export default SubmitButton;

import React from "react";
import { useState } from "react";
import Button from "react-bootstrap/Button";
const endpoint = "http://localhost:5000/api/video";

const DownloadButton = ({ setStatus }) => {
  const [downloadDisabled, setDownloadDisabled] = useState(false);
  const download = async () => {
    setDownloadDisabled(true);
    const res = await fetch(endpoint, {
      method: "POST",
      mode: "cors",
      headers: { "Content-Type": "application/json" },
    });
    setStatus(res.status);
    setDownloadDisabled(false);
  };
  return (
    <Button onClick={download} disabled={downloadDisabled}>
      download
    </Button>
  );
};

export default DownloadButton;

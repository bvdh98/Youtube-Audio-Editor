import React, { useContext } from "react";
import { useState, useEffect } from "react";
import { loadVideo } from "../Functions";
import { statusContext } from "../App";
const Video = () => {
  const { status, vidLink } = useContext(statusContext)
  return (
    <div className="video-container">
      {(status === "success" && vidLink != null) &&
        <video src={vidLink} controls />}
      {status === null && null}
      {status === "downloading" && "downloading..."}
      {status === "invalid-link" && "download failed: please make sure you entered a valid youtube url"}
      {status === "video-exceeds-file-size" && "download failed: the final video exceeds the max file size of 1 GB."}
      {status === "fail" && "download failed"}
    </div>
  );
};

export default Video;

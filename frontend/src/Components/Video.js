import React, { useContext } from "react";
import { useState, useEffect } from "react";
import { loadVideo } from "../Functions";
import { statusContext } from "../App";
const Video = () => {
  const { status } = useContext(statusContext)
  const [videoSrc, setVideoSrc] = useState(null);
  useEffect(() => {
    const fetchVideo = async () => {
      const video = await loadVideo();
      if (video) {
        setVideoSrc(video);
      }
    };
    fetchVideo();
  }, []);
  return (
    <div>
      {status === "success" &&
        <video src={videoSrc} controls width={800} />}
      {status === null && null}
      {status === "downloading" && "downloading..."}
      {status === "invalid-link" && "download failed: please make sure you entered a valid youtube url"}
      {status === "fail" && "download failed"}
    </div>
  );
};

export default Video;

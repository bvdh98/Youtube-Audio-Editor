import React from "react";
import {useState, useEffect} from "react";
import { loadVideo } from "../Functions";
//TODO:disable cra error screen

const Video = ({ status }) => {
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
      {videoSrc
        ? <div>
            {status === "success" &&
              <video src={videoSrc} controls width={800} />}
            {status === null && null}
            {status === "loading" && "loading..."}
            {status === "fail" && "download failed"}
          </div>
        : null}
    </div>
  );
};

export default Video;

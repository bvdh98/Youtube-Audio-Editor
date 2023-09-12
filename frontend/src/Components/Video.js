import React from "react";
import video from "../assets/video/final.mp4";
//TODO:conditionally import the video
const Video = ({ status }) => {
  return (
    <div>
      {status === "success" && <video src={video} controls width={800} />}
      {status === null && null}
      {status === "loading" && "loading..."}
    </div>
  );
};

export default Video;

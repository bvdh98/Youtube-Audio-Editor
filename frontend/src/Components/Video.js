import React from "react";
import video from "../assets/video/final.mp4";
//TODO:conditionally import the video
const Video = () => {
  return <video src={video} controls width={800}/>;
};

export default Video;

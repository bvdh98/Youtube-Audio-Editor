import React, { useState } from "react";
import Button from "react-bootstrap/Button";
import Form from "react-bootstrap/Form";
import SubmitButton from "./SubmitButton";

const SearchForm = () => {
  const [vidLink, setVidLink] = useState(null)
  const [audioLink, setAudioLink] = useState(null)
  return (
    <Form>
      <Form.Group className="mb-3">
        <Form.Label>Enter the URL link of YouTube video</Form.Label>
        <Form.Control placeholder="Video link" onChange={(e)=>setVidLink(e.target.value)}/>
      </Form.Group>
      <Form.Group className="mb-3">
        <Form.Label>
          Enter the URL link of the Youtube video for the audio you want to add to
          the video above
        </Form.Label>
        <Form.Control placeholder="Audio link" onChange={(e)=>setAudioLink(e.target.value)}/>
      </Form.Group>
      <SubmitButton audioLink={audioLink} vidLink={vidLink}></SubmitButton>
    </Form>
  );
};

export default SearchForm;

import React, { useState } from "react";
import Button from "react-bootstrap/Button";
import Form from "react-bootstrap/Form";
import SubmitButton from "./SubmitButton";

const SearchForm = () => {
  const [form, setForm] = useState({});
  const [errors, setErrors] = useState({});

  const setField = (field, value) => {
    //append new form values
    setForm({
      ...form,
      [field]: value,
    });
    // Check and see if errors exist, and remove from error object:
    if (errors[field])
      setErrors({
        ...errors,
        [field]: null,
      });
  };
  const findFormErrors = () => {
    //get paint and status
    const { videoLink, audioLink } = form;
    const newErrors = {};
    //if paint name is null notify user
    if (!videoLink) {
      newErrors.videoLink = "Please enter video link";
    }
    //if status is not selected notify user
    if (!audioLink) {
      newErrors.audioLink = "Please enter audio link";
    }
    return newErrors;
  };
  return (
    <Form>
      <Form.Group className="mb-3">
        <Form.Label>Enter the URL link of YouTube video</Form.Label>
        <Form.Control placeholder="Video link" onChange={(e) => setField("videoLink", e.target.value)} isInvalid={errors.videoLink} />
        <Form.Control.Feedback type="invalid">
          {errors.videoLink}
        </Form.Control.Feedback>
      </Form.Group>
      <Form.Group className="mb-3">
        <Form.Label>
          Enter the URL link of the Youtube video for the audio you want to add to
          the video above
        </Form.Label>
        <Form.Control placeholder="Audio link" onChange={(e) => setField("audioLink", e.target.value)} isInvalid={errors.audioLink} />
        <Form.Control.Feedback type="invalid">
          {errors.audioLink}
        </Form.Control.Feedback>
      </Form.Group>
      <SubmitButton form={form} errors={errors} setErrors={setErrors} findFormErrors={findFormErrors}></SubmitButton>
    </Form>
  );
};

export default SearchForm;

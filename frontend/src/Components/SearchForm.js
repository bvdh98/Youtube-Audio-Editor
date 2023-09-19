import React from "react";
import Button from "react-bootstrap/Button";
import Form from "react-bootstrap/Form";

const SearchForm = () => {
  return (
    <Form>
      <Form.Group className="mb-3">
        <Form.Label>Enter link of Youtube video</Form.Label>
        <Form.Control placeholder="Video link" />
      </Form.Group>
      <Form.Group className="mb-3">
        <Form.Label>
          Enter the link of the Youtube video for the audio you want to add to
          the video above
        </Form.Label>
        <Form.Control placeholder="Video link" />
      </Form.Group>
      <Button variant="primary" type="submit">
        Submit
      </Button>
    </Form>
  );
};

export default SearchForm;

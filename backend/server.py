from flask import Flask, jsonify, make_response
from flask import request
from downloader import *

# create the Flask app
app = Flask(__name__)

@app.post('/api/video')
def query_example():
    # make_new_video()
    print("done")
    return jsonify({'vid_link':'./'})

if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000)
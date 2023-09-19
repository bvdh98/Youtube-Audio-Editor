from flask import Flask, jsonify
from downloader import *
from flask_cors import CORS

# create the Flask app
app = Flask(__name__)
CORS(app)

@app.post('/api/video')
def query_example():
    make_new_video()
    return jsonify({"message":"success"}),200

if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000)
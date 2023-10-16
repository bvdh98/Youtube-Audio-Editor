from flask import Flask, jsonify, request, json
from downloader import *
from flask_cors import CORS
from pytube import exceptions

# create the Flask app
app = Flask(__name__)
CORS(app)

@app.post('/api/video')
def query_example():
    data = json.loads(request.data)
    try:
        make_new_video(data)
        return jsonify({"message":"success"}),200
    except exceptions.RegexMatchError:
        return jsonify({"message":"invalid-link"}),500
    except Exception as e:
        print(f'Unexpected {e}, {type(e)=}')
        return jsonify({"message":"fail"}),500


if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000)
from flask import Flask, jsonify, request, json, session
from downloader import *
from flask_cors import CORS
from pytube import exceptions
import asyncio
from dotenv import load_dotenv
import os

# create the Flask app
app = Flask(__name__)
CORS(app)
load_dotenv('.env')
app.secret_key = os.getenv('SECRET_KEY')

@app.get('/api/downloadstatus')
def get_status():
    try:
        return jsonify({'isDownloading':session['isDownloading']}),200
    except KeyError:
        return jsonify({'isDownloading':False})

@app.post('/api/video')
async def get_video():
    data = json.loads(request.data)
    try:
        session['isDownloading'] = True
        await make_new_video(data)
        session['isDownloading'] = False
        return jsonify({"message":"success"}),200
    except exceptions.RegexMatchError:
        return jsonify({"message":"invalid-link"}),500
    except Exception as e:
        print(f'Unexpected {e}, {type(e)=}')
        return jsonify({"message":"fail"}),500


if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000)
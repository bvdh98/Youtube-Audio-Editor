from flask import Flask, jsonify, request, json, session
from downloader import *
from flask_cors import CORS
from pytube import exceptions
from dotenv import load_dotenv
import os
from google_cloud_funcs import authenticate_implicit_with_adc, upload_blob
final_video = 'C:/Program Files/ffmpeg/bin/downloads/videos/final.mp4'
storage_video_link = "https://storage.cloud.google.com/youtube-audio-editor-videos/final.mp4"

app = Flask(__name__, static_url_path='')
CORS(app, supports_credentials=True)
load_dotenv('.env')
app.secret_key = os.getenv('SECRET_KEY')
authenticate_implicit_with_adc()

@app.route('/')
def index():
    return app.send_static_file('index.html')


@app.get('/api/downloadstatus')
def get_status():
    if 'isDownloading' in session:
        return jsonify({'isDownloading': session['isDownloading']}), 200
    else:
        return jsonify({'isDownloading': False})


@app.post('/api/video')
async def get_video():
    data = json.loads(request.data)
    try:
        session['isDownloading'] = True
        video = make_new_video(data)
        if video['exceeds_max_size']:
            return jsonify({"message": "video-exceeds-file-size"}), 500
        else:
            upload_blob(bucket_name='youtube-audio-editor-videos',
                    source_file_name=video['path'], destination_blob_name='final.mp4')
        return jsonify({"message": "success","vidLink":storage_video_link}), 200
    except exceptions.RegexMatchError:
        return jsonify({"message": "invalid-link"}), 500
    except Exception as e:
        print(f'Unexpected {e}, {type(e)=}')
        return jsonify({"message": "fail"}), 500
    finally:
        session['isDownloading'] = False

if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000)

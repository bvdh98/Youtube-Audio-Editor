from pytube import YouTube
from moviepy.editor import *
import subprocess as sp
import os.path
# TODO:make video and audio same length
project_wd = 'C:/Users/benha/OneDrive/Desktop/dev/YouTube-Audio-Editor/backend'
fmpeg_dir = 'C:/Program Files/ffmpeg/bin/downloads'
video_path = f'{fmpeg_dir}/videos'
audio_path = f'{fmpeg_dir}/audio'
#max size in bytes (1gb)
MAX_DOWNLOAD_SIZE = 1073741824
# TODO: make general download function
# TODO: fix potential issue with asking to sign in for age restricted videos at first
# TODO: change links for prod
# TODO: upload to bucket instead of local download. Try using process
# TODO: check if final vid is too large


def clean_up_directory(file_path):
    if os.path.isfile(file_path):
        os.remove(file_path)

def download_vid(vid_link):
    video = YouTube(vid_link, use_oauth=True,
                    allow_oauth_cache=True)
    video = video.streams.get_highest_resolution()
    print("downloading vid")
    print(video_path)
    video.download(video_path, filename='video.mp4')
    print("video was downloaded successfully")


def download_audio(audio_link):
    video = YouTube(audio_link)
    stream = video.streams.filter(only_audio=True).first()
    print("downloading audio")
    print(audio_path)
    stream.download(audio_path, filename='audio.mp3')
    print("audio was downloaded successfully")


def make_new_video(data):
    final_vid_path = f'{video_path}/final.mp4'
    video = {'path':final_vid_path,'exceeds_max_size':False}
    download_vid(data['vidLink'])
    download_audio(data['audioLink'])
    print('final download')
    print(final_vid_path)
    sp.run(
        f'ffmpeg -i "{video_path}"/video.mp4 -i "{audio_path}"/audio.mp3 -c:v copy -map 0:v -map 1:a -y "{final_vid_path}"')
    if os.path.getsize(final_vid_path) > MAX_DOWNLOAD_SIZE:
        video['exceeds_max_size':True]
    return video


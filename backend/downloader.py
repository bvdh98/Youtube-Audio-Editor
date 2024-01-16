from pytube import YouTube
from moviepy.editor import *
import subprocess as sp
# TODO:make video and audio same length
# video_link = "https://www.youtube.com/watch?v=_3trjVGVP3k"
# audio_link = "https://www.youtube.com/watch?v=iRA82xLsb_w"
video_folder_path = "downloads/videos"
audio_folder_path = "downloads/audio"
# vid_title = ''
# audio_title = ''
# illegal_chars = ["<", ">", ":", "/", "\\", "|", "?", "*", "\"", "\'"]
# TODO: make general download function
# TODO: fix potential issue with asking to sign in for age restricted videos at first
# TODO: change links for prod


def download_vid(vid_link):
    video = YouTube(vid_link, use_oauth=True,
                    allow_oauth_cache=True)
    video = video.streams.get_highest_resolution()
    video.download(filename=f"./{video_folder_path}/video.mp4")
    print("video was downloaded successfully")


def download_audio(audio_link):
    video = YouTube(audio_link)
    stream = video.streams.filter(only_audio=True).first()
    stream.download(filename=f"./{audio_folder_path}/audio.mp3")
    print("audio was downloaded successfully")


def make_new_video(data):
    wd = 'C:/Users/benha/OneDrive/Desktop/dev/YouTube-Audio-Editor'
    output_vid = f"{wd}/backend/video/final.mp4"
    download_vid(data['vidLink'])
    download_audio(data['audioLink'])
    video = f'{wd}/backend/{video_folder_path}/video.mp4'
    audio = f'{wd}/backend/{audio_folder_path}/audio.mp3'
    sp.run(
        f'ffmpeg -i {video} -i {audio} -c:v copy -map 0:v -map 1:a -y {output_vid}')

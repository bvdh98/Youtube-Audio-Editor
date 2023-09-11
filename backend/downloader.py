from pytube import YouTube
from moviepy.editor import *
import os

# TODO:make video and audio same length
# TODO:handle error when video is age restricted
video_link = "https://www.youtube.com/watch?v=_3trjVGVP3k&t=194s"
audio_link = "https://www.youtube.com/watch?v=iRA82xLsb_w"
video_folder_path = "./downloads/videos"
audio_folder_path = "./downloads/audio"
vid_title = ''
audio_title = ''
illegal_chars = ["<", ">", ":", "/", "\\", "|", "?", "*", "\"", "\'"]
# TODO: make general download function
# TODO: check if video and audio have already been downloaded
# TODO: make faster

def download_vid():
    video = YouTube(video_link)
    global vid_title
    vid_title = video.title + '.mp4'
    vid_title = "".join(
        [char if char not in illegal_chars else "" for char in vid_title])
    video = video.streams.get_highest_resolution()
    try:
        video.download(video_folder_path)
    except Exception as e:
        print(e)
    print("video was downloaded successfully")


def download_audio():
    video = YouTube(audio_link)
    audio_clip = video.streams.get_highest_resolution()
    global audio_title
    audio_title = video.title + '.mp4'
    audio_title = "".join(
        [char if char not in illegal_chars else "" for char in audio_title])
    try:
        audio_clip.download(audio_folder_path)
    except Exception as e:
        print(e)
    print("audio was downloaded successfully")


def make_new_video():
    download_vid()
    download_audio()
    # Input audio file
    audio = AudioFileClip(f'{audio_folder_path}/{audio_title}')
    # Input video file
    video = VideoFileClip(f'{video_folder_path}/{vid_title}')
    # adding external audio to video
    final_video = video.set_audio(audio)
    # Extracting final output video
    final_video.write_videofile("../frontend/src/assets/video/final.mp4", threads=8, fps=24)


if __name__ == '__main__':
    make_new_video()

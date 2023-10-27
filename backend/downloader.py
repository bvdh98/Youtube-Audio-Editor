from pytube import YouTube
from moviepy.editor import *

# TODO:make video and audio same length
# TODO:handle error when video is age restricted
# video_link = "https://www.youtube.com/watch?v=_3trjVGVP3k"
# audio_link = "https://www.youtube.com/watch?v=iRA82xLsb_w"
video_folder_path = "./downloads/videos"
audio_folder_path = "./downloads/audio"
vid_title = ''
audio_title = ''
illegal_chars = ["<", ">", ":", "/", "\\", "|", "?", "*", "\"", "\'"]
# TODO: make general download function
# TODO: check if video and audio have already been downloaded
# TODO: make faster (remove downloader visual in terminal)


def download_vid(vid_link):
    video = YouTube(vid_link, use_oauth=True,
                    allow_oauth_cache=True)
    global vid_title
    vid_title = video.title + '.mp4'
    vid_title = "".join(
        [char if char not in illegal_chars else "" for char in vid_title])
    video = video.streams.get_highest_resolution()
    video.download(video_folder_path)
    print("video was downloaded successfully")


def download_audio(audio_link):
    video = YouTube(audio_link)
    audio_clip = video.streams.get_highest_resolution()
    global audio_title
    audio_title = video.title + '.mp4'
    audio_title = "".join(
        [char if char not in illegal_chars else "" for char in audio_title])
    audio_clip.download(audio_folder_path)
    print("audio was downloaded successfully")


def make_new_video(data):
    download_vid(data['vidLink'])
    download_audio(data['audioLink'])
    # Input audio file
    audio = AudioFileClip(f'{audio_folder_path}/{audio_title}')
    # Input video file
    video = VideoFileClip(f'{video_folder_path}/{vid_title}')
    # adding external audio to video
    final_video = video.set_audio(audio)
    # Extracting final output video
    final_video.write_videofile(
        "../frontend/src/video/final.mp4", threads=8, fps=24)


if __name__ == '__main__':
    make_new_video()

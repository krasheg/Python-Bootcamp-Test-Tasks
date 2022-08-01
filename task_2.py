# This file contains a function that converts video to GIF and returns it abs path
import requests
from moviepy.editor import VideoFileClip
import itertools
from pathlib import Path
import os


def video_to_gif(link: str, filename: str = 'TikTok Example'):
    """
    This function downloads video from url and converts it into .gif and returns it`s abs path
    :param link: url for video
    :param filename: name of video
    :return: abs path to .gif file
    """
    # check if filename has .mp4
    if not filename.endswith('.mp4'):
        filename += '.mp4'

    # create response object
    r = requests.get(link, stream=True)

    # download started
    with open(filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024 * 1024):
            if chunk:
                f.write(chunk)
    # using moviepy lib for convert .mp4 to gif
    videoclip = VideoFileClip(filename)
    # creating a filename for .gif and try to save it
    path = Path(filename.replace(' ', '-').split(".")[0] + ".gif")
    for i in itertools.count(1):
        new_path = path.parent / (path.stem + f'-{i}' + path.suffix)
        if not new_path.exists():
            videoclip.write_gif(new_path, fps=15)
            return os.path.abspath(new_path)


if __name__ == "__main__":
    link = "https://v16m-webapp.tiktokcdn-us.com/ed129ecb01ab00e202682e99f68a9288/62e7cb0d/video/tos/useast5/tos" \
           "-useast5-pve-0068-tx/d69985b1677b4a73a584b56d604011ca/?a=1988&ch=0&cr=0&dr=0&lr=tiktok_m&cd=0%7C0%7C1%7C0" \
           "&cv=1&br=4020&bt=2010&cs=0&ds=3&ft=ebtHKH-qMyq8ZjFl1we2N9befl7Gb&mime_type=video_mp4&qs=0&rc" \
           "=OTU4MzU0NzVnaDpnOGg8OEBpajM5Z2c6ZmYzZTMzZzczNEAuMC9jLWBgNmExMzJfY18tYSMxX28vcjRnMGRgLS1kMS9zcw%3D%3D&l" \
           "=20220801064449EF653E99EF32BC2EAB55 "
    print(video_to_gif(link))

# This file contains a function that converts video to GIF and returns it abs path
from moviepy.editor import VideoFileClip
import itertools
from pathlib import Path
import os


def video_to_gif(link: str, filename: str = 'TikTok Example'):
    """
    This function converts video into .gif and returns it`s abs path
    :param link: url for video
    :param filename: name for gif
    :return: abs path to .gif file
    """
    # using moviepy lib for convert .mp4 to gif
    try:
        videoclip = VideoFileClip(link)
    except Exception as e:
        print(e, "Can`t use this link")
    # creating a filename for .gif and save it
    path = Path(filename.replace(' ', '-').split(".")[0] + ".gif")
    for i in itertools.count(1):
        new_path = path.parent / (path.stem + f'-{i}' + path.suffix)
        if not new_path.exists():
            try:
                videoclip.write_gif(new_path, fps=5)  # for faster convertation
            except Exception as e:
                print(e, 'Can`t convert this video to .gif')
            return os.path.abspath(new_path)


if __name__ == "__main__":
    link = "https://v16-webapp.tiktok.com/ac8370e95848330ef7e530b461ea1ef3/62e87c9a/video/tos/maliva/tos-maliva-ve" \
           "-0068c799-us/0f9740522a1c45f092da7b8eb42a0ef3/?a=1988&ch=0&cr=0&dr=0&lr=tiktok_m&cd=0%7C0%7C1%7C0&cv=1&br" \
           "=1948&bt=974&btag=80000&cs=0&ds=3&ft=eXd.6H-oMyq8Z-MoKwe2NP0Aol7Gb&mime_type=video_mp4&qs=0&rc" \
           "=OTk3aGk4M2U2Z2kzPDtmNEBpM3M4PDw6Zjw2PDMzZzczNEA2YWFfMGItXi0xXzU0Ml5iYSMxNWAvcjRvamJgLS1kMS9zcw%3D%3D&l" \
           "=20220801192148010192168091065B216A "
    print(video_to_gif(link))

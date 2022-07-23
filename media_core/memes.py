from moviepy.editor import *
from moviepy.video.fx.all import crop


class WidePutin:
    async def create(self, file_path: str) -> None:
        video = VideoFileClip(file_path)
        audio = AudioFileClip(
            'static/memes_sound/wide_putin.mp3').subclip(40, video.duration + 40)
        os.remove(file_path)
        w, h = video.size
        video = video.resize((w * 2, h))
        video = video.crop(x1=w/2, y1=0, x2=w*1.5, y2=h)
        video = video.set_audio(audio)
        video.write_videofile(file_path)
        video.close()

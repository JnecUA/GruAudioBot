import os
from media_core.ffmpeg import FFmpeg


class WidePutin:
    async def create(self, file_path: str, ratio: int) -> str:
        output_path = file_path[:-4] + '_output' + file_path[-4:]
        putin_sound_path = "static/memes_sound/wide_putin.mp3"
        change_audio_args = f'-i {putin_sound_path} -c:a copy -map 0:v:0 -map 1:a:0 -shortest'
        resize_args = f'-vf scale=iw*{ratio}:ih'
        crop_args = f'crop=iw*{round(1/ratio, 2)}:ih'
        threads_args = '-threads 4'
        command = f'ffmpeg -i {file_path} {change_audio_args} {resize_args},{crop_args} {output_path} {threads_args}'
        _ = await FFmpeg().exec(command)
        os.remove(file_path)
        return output_path

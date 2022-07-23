from media_core import ffmpeg
import os

from media_core.ffmpeg import FFmpeg


class WidePutin:
    async def create(self, file_path: str) -> str:
        output_path = file_path.split('.')[0]+'_output.'+file_path.split('.')[1]
        putin_sound_path = "static/memes_sound/wide_putin.mp3"
        change_audio_args = f'-i {putin_sound_path} -c:a copy -map 0:v:0 -map 1:a:0 -shortest'
        resize_args = '-vf scale=iw*2:ih'
        crop_args = '-vf crop=iw*0.75:ih:iw*.125:ih'
        threads_args = '-threads 4'
        command = f'ffmpeg -i {file_path} {change_audio_args} {resize_args} {crop_args} {output_path} {threads_args}'
        _ = FFmpeg().exec(command)
        os.remove(file_path)
        return output_path

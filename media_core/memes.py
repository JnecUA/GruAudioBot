from media_core.shell import Shell


class WidePutin:
    async def create(self, file_path: str, ratio: int) -> str:
        output_path = file_path[:-4] + '_output' + file_path[-4:]
        putin_sound_path = "static/memes_sound/wide_putin.mp3"
        change_audio_args = f'-i {putin_sound_path} -map 0:v:0 -map 1:a:0 -shortest'
        resize_args = f'-vf scale=iw*{ratio}:ih,setsar=1:1'
        crop_args = f'crop=iw*{round(1/ratio, 2)}:ih'
        threads_args = '-threads 4'
        command = f'ffmpeg -loglevel panic -i {file_path} {change_audio_args} {resize_args},{crop_args} {output_path} {threads_args}'
        process = await Shell().exec(command)
        await process.communicate()
        return output_path

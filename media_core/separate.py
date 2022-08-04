from media_core.shell import Shell


class Separate:
    async def create(self, file_path: str, stems: str) -> str:
        file_name = file_path.split('/')[-1]
        output_path = file_path.split(
            file_name)[0] + 'output/' + file_name[:-4]
        command = f'cd static/separate && spleeter separate -c mp3 -p spleeter:{stems} -o output {file_name}'
        process = await Shell().exec(command)
        await process.communicate()
        return output_path

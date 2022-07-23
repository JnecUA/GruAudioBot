import subprocess
import asyncio
class FFmpeg:
    async def exec(self, command: str):
        process = subprocess.Popen(command.split())
        output, error = process.communicate()
        print(output)
        print(error)

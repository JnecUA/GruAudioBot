import asyncio


class FFmpeg:
    async def exec(self, command: str):
        process = await asyncio.create_subprocess_shell(command)
        return process

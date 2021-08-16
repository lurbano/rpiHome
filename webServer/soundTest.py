import asyncio
import subprocess

async def tick(n):
    i = 0
    while i < n:
        await asyncio.sleep(1)
        print(i)
        i++


#subprocess.Popen('omxplayer -o local 1.mp4', shell=True)

asyncio.run(tick(5))

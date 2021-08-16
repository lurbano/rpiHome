import asyncio
import subprocess
import time

alarm = {'h': 0, 'm': 41, 's': 0}

async def tick(a):
    while 1:
        now = time.localtime()
        h = now.tm_hour
        m = now.tm_min
        s = now.tm_sec
        await asyncio.sleep(0.5)
        print(f'{h}:{m}:{s}')
        if (h == a["h"]) and (m == a["m"]) and (s == a["s"]):
            print("Ring...")
            return "alarm"




asyncio.run(tick(alarm))

subprocess.Popen('omxplayer -o local 1.mp4', shell=True)

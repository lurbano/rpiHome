import asyncio
import subprocess

alarm = {h: 0, m: 36, s: 0}

async def tick(a):
    while 1:
        now = time.localtime()
        h = now.tm_hour
        m = now.tm_min
        s = now.tm_sec
        await asyncio.sleep(0.5)
        print(f'{h}:{m}:{s})
        if (h == a["h"]) and (m == a["m"]) and (s = a["s"]):
            print("Ring...")
            return "alarm"


#subprocess.Popen('omxplayer -o local 1.mp4', shell=True)

asyncio.run(tick(alarm))

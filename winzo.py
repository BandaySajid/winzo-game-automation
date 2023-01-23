import numpy as np
import mss
import pyautogui
import time
import threading
import subprocess

sct = mss.mss()
points = [(150, 139, 471, 276), (115, 238, 355, 583), (127, 336, 393, 894), (336, 139, 1045, 273), (249, 212, 776, 502), (261, 317, 811, 825), (469, 161, 1459, 335), (396, 253, 1229, 634), (496, 323, 1544, 853), (619, 123, 1930, 213), (578, 225, 1796, 546), (621, 340, 1930, 904)]
# points = [(471, 276), (355, 583), (393, 894), (1045, 273), (776, 502), (811, 825), (1459, 335), (1229, 634), (1544, 853), (1930, 213), (1796, 546), (1930, 904)]

img = []

def checkColor(index):
    while True:
        if(len(img) != 0):
            point = points[index]
            position = (point[0], point[1])
            color = img[point[1], point[0]]
            if color[0] > 180:
                print(f'detected color and clicking at {position}')
                subprocess.run(['xdotool', 'mousemove', f'{point[0]}', f'{point[1]}', 'click', '1'])
                time.sleep(0.9)

                

for i, point in enumerate(points):
    t = threading.Thread(target=checkColor, args=(i,))
    t.start()

while True:
    img = np.array(sct.grab(sct.monitors[0]))

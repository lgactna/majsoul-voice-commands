import numpy as np
import cv2
from mss import mss
from PIL import Image

#see https://stackoverflow.com/questions/35097837/capture-video-data-from-screen-in-python

mon = {'top': 0, 'left': 0, 'width': 800, 'height': 800}

sct = mss()

while 1:
    screenshot = sct.grab(mon)
    #https://python-mss.readthedocs.io/api.html#mss.tools.mss.base.ScreenShot
    #img = Image.frombytes("RGB", (screenshot.width, screenshot.height), screenshot.rgb) #processing, etc...
    #sct.get_pixels(mon)
    #img = Image.frombytes('RGB', (sct.width, sct.height), sct.image)
    cv2.imshow('test', np.array(screenshot))
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
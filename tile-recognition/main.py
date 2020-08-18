import cv2
import numpy as np
#from matplotlib import pyplot as plt
from mss import mss
from PIL import Image

template = cv2.imread('C:/Users/Kisun/Desktop/majsoul-voice-commands/tiles/1m.png',0)
w, h = template.shape[::-1]

# All the 6 methods for comparison in a list
methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
            'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

mon = {'top': 0, 'left': 0, 'width': 800, 'height': 800}

sct = mss()

while True:
    meth = 'cv2.TM_CCOEFF'
    #https://stackoverflow.com/questions/32592950/python-opencv-template-matching-error
    #https://stackoverflow.com/questions/48818032/python-opencv-matchtemplate-error?rq=1
    img = np.array(sct.grab(mon))
    #print(img.dtype)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #print(img_gray.dtype)

    method = eval(meth)
    res = cv2.matchTemplate(img_gray, template, method)

    # Apply template Matching
    res = cv2.matchTemplate(img_gray, template, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)

    #the output image doesn't need to be gray as well
    cv2.rectangle(img, top_left, bottom_right, 255, 2)
    cv2.imshow('test', img)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
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

#because of the resize issue, maybe look into having the user define the size of the tiles in their hands?
#then use pillow to split and resize a single, long png of every tile (or resize every png)

while True:
    #https://stackoverflow.com/questions/32592950/python-opencv-template-matching-error
    #https://stackoverflow.com/questions/48818032/python-opencv-matchtemplate-error?rq=1
    img = np.array(sct.grab(mon))
    #print(img.dtype)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #print(img_gray.dtype)

    colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (0, 255, 255), (255, 255, 255)]
    index = 0
    for i in range(0, len(methods)):
        method = eval(methods[i])

        # Apply template Matching
        res = cv2.matchTemplate(img_gray, template, method)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

        # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
        if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
            top_left = min_loc
        else:
            top_left = max_loc

        #print(min_loc)
        #print(max_loc)
        #print(h)
        #observe here how it always takes the size of the original template
        #this may or may not be bigger than desired
        bottom_right = (top_left[0] + w, top_left[1] + h)

        #the output image doesn't need to be gray as well
        #we draw the rectangle on top of the original
        #colors are in BGR!!
        cv2.rectangle(img, top_left, bottom_right, colors[i], 2)
    cv2.imshow('test', img)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
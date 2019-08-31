import cv2
import numpy as np
import mss
import time

sct = mss.mss()
bbox = {'top': 50, 'left': 0, 'width': 800, 'height': 600}


def process(image):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    processed_image = cv2.Canny(gray_image, 200, 300)
    return processed_image


def main():
    while True:
        # last_time = time.time()
        sct_img = sct.grab(bbox)
        src = np.array(sct_img)
        # print(src.shape)
        # print("loop took {} seconds", format(time.time() - last_time))
        cv2.imshow('test', process(src))
        key = cv2.waitKey(1)
        if key is 27:
            break
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()

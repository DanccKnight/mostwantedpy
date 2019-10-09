import cv2
import numpy as np
import mss
from pykeyboard import PyKeyboard
import time

sct = mss.mss()
bbox = {'top': 50, 'left': 0, 'width': 800, 'height': 600}
k = PyKeyboard()


def draw_lines(img, lines):
    try:
        for line in lines:
            #print(line)
            coordinates = line[0]
            cv2.line(img, (coordinates[0], coordinates[1]), (coordinates[2], coordinates[3]), [255, 255, 255], 3)
    except:
        pass


def process(image):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    processed_image = cv2.Canny(gray_image, 200, 300)
    processed_image = cv2.GaussianBlur(processed_image, (5, 5), 0)
    vertices = np.array([[0, 600], [0, 400], [250, 300], [450, 300], [800, 400], [800, 600]])
    processed_image = roi(processed_image, [vertices])
    lines = cv2.HoughLinesP(processed_image, 1, np.pi / 180, 100, 20, 15)
    draw_lines(processed_image, lines)
    return processed_image


def roi(img, vertices):
    mask = np.zeros_like(img)
    cv2.fillPoly(mask, vertices, 255)
    masked = cv2.bitwise_and(img, mask)
    return masked


def main():
    for i in list(range(5))[::-1]:
        print(i + 1)
        time.sleep(1)

    while True:
        #k.press_key('a')
        # last_time = time.time()
        sct_img = sct.grab(bbox)
        src = np.array(sct_img)
        # print(src.shape)
        # print("loop took {} seconds", format(time.time() - last_time))
        cv2.imshow('test', process(src))
        key = cv2.waitKey(1)
        if key is 27:
            #k.release_key('a')
            break
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
import numpy as np
import cv2
import time
from colorlabeler import density, cubestr
import kociemba

def screen_record():
    last_time = time.time()
    cv2.startWindowThread()

    cap = cv2.VideoCapture(0)

    faces = "FUDLRB"
    idx = 0

    data = {
        "F" : ["", "", "", "", "", "", "", "", ""],
        "U" : ["", "", "", "", "", "", "", "", ""],
        "D" : ["", "", "", "", "", "", "", "", ""],
        "L" : ["", "", "", "", "", "", "", "", ""],
        "R" : ["", "", "", "", "", "", "", "", ""],
        "B" : ["", "", "", "", "", "", "", "", ""]
    }

    while(True):
        _, img = cap.read()
        last_time = time.time()
        img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        colors = {
            "red" : (0, 0, 255),
            "blue" : (255, 0, 0),
            "green" : (0, 255, 0),
            "yellow" : (0, 255, 255),
            "white" : (255, 255, 255),
            "orange" : (0, 165, 255)
        }

        offset = 75
        z = 0
        for i in (-1, 0, 1):
            for j in (-1, 0, 1):
                px = 358 + j * offset
                py = 280 + i * offset

                maxDens = [0, "white"]
                crop = img_hsv[(py-35):(py+35), (px-35):(px+35)]
                for k in ("red", "blue", "green", "yellow", "white", "orange"):
                    d = density(crop, k)
                    if d > maxDens[0]:
                        maxDens[0] = d
                        maxDens[1] = k

                cv2.circle(img, (px, py), 5, colors[maxDens[1]], -1)
                data[faces[idx]][z] = maxDens[1][0]
                z += 1

        cv2.imshow(faces[idx] + ' Face', img)
        key = cv2.waitKey(1)
        if key == ord('q'):
            break
        elif key == ord('h'):
            idx += 1
            if idx == len(faces):
                print(kociemba.solve(cubestr(data)))
                break

    cv2.destroyAllWindows()
    cap.release()

screen_record()


import cv2
import numpy as np

# I want to make sea to red :D
vid = cv2.VideoCapture(r'F:\computer-vision-area\practices\data\blue-sea.mp4')
w = int(vid.get(3))
h = int(vid.get(4))
out = cv2.VideoWriter(r'data\red-sea.mp4', cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'),
                      10.0, (w, h))

lower_blue = np.array([70, 150, 90])
upper_blue = np.array([130, 255, 255])

while vid.isOpened():
    ret, frame = vid.read()

    if not ret:
        print('video is finished')
        break

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    frame2 = frame.copy()
    frame2[mask > 0] = (48, 48, 240)
    out.write(frame2)
    cv2.imshow('frame', frame2)
    if cv2.waitKey(1) == ord('q'):
        break
vid.release()
out.release()
cv2.destroyAllWindows()

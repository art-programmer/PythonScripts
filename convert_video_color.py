import cv2
import sys
import numpy as np

video = cv2.VideoCapture(sys.argv[1])
index = 0
while True:
    print(index)
    ret, image = video.read()
    if not ret:
        break
    backgroundMask = np.all(image <= 1, axis=-1)
    backgroundMask = np.expand_dims(backgroundMask, axis=-1)
    image = image * (1 - backgroundMask) + 255 * backgroundMask
    cv2.imwrite('test/frame_%04d.png' % index, image)
    index += 1
    continue

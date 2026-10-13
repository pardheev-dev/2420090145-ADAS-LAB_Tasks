# PROGRAM 6: Traffic Sign Detection System
# Detects traffic signs based on their colour using HSV thresholding.

import cv2
import numpy as np

image = cv2.imread("traffic_signs.jpg")
if image is None:
    raise FileNotFoundError("traffic_signs.jpg not found - put a sign image in this folder")

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# HSV ranges for the common sign colours
red1 = cv2.inRange(hsv, (0, 80, 80), (10, 255, 255))
red2 = cv2.inRange(hsv, (170, 80, 80), (180, 255, 255))
red = red1 | red2
blue = cv2.inRange(hsv, (90, 80, 70), (130, 255, 255))
yellow = cv2.inRange(hsv, (18, 80, 80), (40, 255, 255))

combined = red | blue | yellow

# Clean up the mask
kernel = np.ones((5, 5), np.uint8)
combined = cv2.morphologyEx(combined, cv2.MORPH_OPEN, kernel)
combined = cv2.morphologyEx(combined, cv2.MORPH_CLOSE, kernel)

contours, _ = cv2.findContours(combined, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

count = 0
for cnt in contours:

    area = cv2.contourArea(cnt)
    if area < 500:
        continue

    perimeter = cv2.arcLength(cnt, True)
    if perimeter == 0:
        continue

    # Signs are round or nearly round
    circularity = 4 * np.pi * area / (perimeter * perimeter)
    if circularity < 0.35:
        continue

    x, y, w, h = cv2.boundingRect(cnt)

    # Signs are roughly as wide as they are tall - this rejects
    # poles, railings and other tall thin coloured objects
    aspect_ratio = w / float(h)
    if not 0.6 < aspect_ratio < 1.6:
        continue

    count += 1
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.putText(image, "Traffic Sign", (x, y - 8),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 255), 2)

print("Traffic signs detected:", count)

cv2.imwrite("output.jpg", image)
cv2.imshow("Traffic Sign Detection", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

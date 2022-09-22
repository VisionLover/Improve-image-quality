import cv2
import numpy as np

image = cv2.imread("photo_2022-09-20_02-14-52.jpg")
print(np.shape(image))
h, w, ch_numbers = np.shape(image)
lower = (180, 180, 180)  # lower bound for each channel
upper = (255, 255, 255)  # upper bound for each channel
lower1 = (180, 180, 180)  # lower bound for each channel
upper1 = (255, 255, 255)  # upper bound for each channel


# create the mask and use it to change the colors
mask = cv2.inRange(image, lower, upper)
image[mask != 0] = [255,255,255]
cv2.imwrite("Rotation.png", image)
image = cv2.imread("Rotation.png")
image = cv2.medianBlur(image, 9)
_, image = cv2.threshold(image, 185, 255, cv2.THRESH_BINARY)
cv2.imwrite("Captcha.png", image)

count = 0
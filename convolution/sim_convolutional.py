
import matplotlib.pyplot as plt
import cv2 as cv
import pylab
import numpy as np


img = cv.imread("flower.jpeg")
fil = np.array(([-1, -1, -1, 0, 1], [-1, -1, 0, 1, 1], [-1, 0, 1, 1, 1]))  # Convolutional operator
img2 = cv.filter2D(img, -1, fil)
cv.imshow("after", img2)
cv.imshow("origin", img)
cv.imwrite("convolutional.png", img2)
cv.waitKey(0)




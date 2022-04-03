import cv2
import numpy as np
from matplotlib import pyplot as plt


def classify_gray_hist(image1, image2, size=(256, 256)):
    """
    Calculating the similarity of two picture by comparing the gray histogram
    :param image1:
    :param image2:
    :param size:
    :return: the degree
    """
    image1 = cv2.resize(image1, size)
    image2 = cv2.resize(image2, size)
    hist1 = cv2.calcHist([image1], [0], None, [256], [0.0, 255.0])
    hist2 = cv2.calcHist([image2], [0], None, [256], [0.0, 255.0])
    plt.plot(range(256), hist1, 'r')
    plt.plot(range(256), hist2, 'b')
    plt.show()
    degree = 0.0
    for i in range(len(hist1)):
        if hist1[i] != hist2[i]:
            degree = degree + (1 - abs(hist1[i] - hist2[i]) / max(hist1[i], hist2[i]))
        else:
            degree = degree + 1
    degree = degree / len(hist1)
    return degree


if __name__ == '__main__':
    img1 = cv2.imread("flower.jpeg")
    img2 = cv2.imread("flowers.jpeg")
    # cv2.imshow('img1', img1)
    # cv2.imshow('img2', img2)
    degrees = classify_gray_hist(img1, img2)
    print (degrees)
    cv2.waitKey(0)

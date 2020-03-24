import cv2
import numpy as np

def get_grayscale(image):
    return cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)


def remove_noise(image):
    return cv2.medianBlur(image,5)

def thresholding(image):
    return cv2.threshold(image,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)[1]

def opening(image):
    kernel = np.ones((5,5),np.uint8)
    return cv2.morphologyEx(image,cv2.MORPH_OPEN,kernel)

def canny(image):
    return cv2.Canny(image,100,200)
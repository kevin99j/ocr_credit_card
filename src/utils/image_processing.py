from skimage import color, measure, morphology, exposure
from skimage.feature import canny
from skimage.filters import threshold_otsu, threshold_local, sobel
from skimage.restoration import denoise_bilateral
import numpy as np
from skimage.transform import rescale, resize, rotate

# convierte imagenes rgb a gris


def image_to_gray(image):
    return color.rgb2gray(image)

# es muy util si el fondo es uniforme
def threshold_image(image):
    thresh = threshold_otsu(image)
    binary = image <= thresh
    return binary


def denoise_image(image, multichann):
    return denoise_bilateral(image, multichannel=multichann)


def edges_detection(image):
    return canny(image=image, sigma=9)


def image_rescale(image, degree, multichanel):
    return rescale(image=image, scale=degree, anti_aliasing=True, multichannel=multichanel)


def image_rotate(image, degree):
    return rotate(image, degree)


def image_rezise(image, height, width):
    return resize(image, (height, width), anti_aliasing=True)


def image_erosion(image):
    return morphology.binary_erosion(image)


def contrast(image):
    return exposure.equalize_adapthist(image=image, clip_limit=0.09)


def contours_of_image(image):
    contours = measure.find_contours(image, 0.8)
    return contours


def contours_sobel(image):
    return sobel(image)


def thresh_local(image):
    block_size = 35
    local = threshold_local(image, block_size, offset=0.3)
    binary = image > local
    return binary

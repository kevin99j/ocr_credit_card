from utils.image_visualization import show_image, show_contours
import utils.image_processing as imgP 
from core.tesseract_app import get_image_text
from PIL import Image
import numpy as np
import cv2


def extract_text(image):
    image = cv2.imread(image)
    #show_image(image, tittle='normal image', cmap='plasma')
    img_gray = imgP.image_to_gray(image)
   # show_image(image=img_gray, tittle='gray_image', cmap='gray')
    betterQ = improve_quality(img_gray)
    improve_quality_contrast(img_gray)
   # show_image(betterQ, tittle='better quality', cmap='gray')
    #print(get_image_text(Image.fromarray(np.uint8(betterQ))))
    #print(get_image_text(image))


def improve_quality(image):
    height = image.shape[0]*2
    width = image.shape[1]*2
    image = imgP.image_rezise(image, height, width)
   # show_image(image=contrasted, tittle='contrast', cmap='gray')
    thresh = imgP.threshold_image(image)
    show_image(image=thresh, tittle='tresh', cmap='gray')
    # denoise image
    denoised = imgP.denoise_image(thresh, False)
   # show_image(image=denoised, tittle='denoised', cmap='gray')
    edges = imgP.edges_detection(denoised)
    show_image(image=edges, tittle='edges canny', cmap='gray')
    return edges


def improve_quality_contrast(image):
    height = image.shape[0]*2
    width = image.shape[1]*2
    image = imgP.image_rezise(image, height, width)
    contrasted = imgP.contrast(image)
   # show_image(image=contrasted, tittle='contrast', cmap='gray')
    thresh = imgP.threshold_image(contrasted)
    show_image(image=thresh, tittle='tresh contrast', cmap='gray')
    # denoise image
    denoised = imgP.denoise_image(thresh, False)
   # show_image(image=denoised, tittle='denoised', cmap='gray')
    edges = imgP.edges_detection(denoised)
    show_image(image=edges, tittle='edges canny contrast', cmap='gray')
    return edges
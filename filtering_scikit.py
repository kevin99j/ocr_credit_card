from skimage.filters import threshold_otsu, threshold_local
from skimage import color, feature
import utils as utils 


def threshold_scikit(image):
    image_gray = color.rgb2gray(image)
    thresh = threshold_otsu(image_gray)
    binary = image_gray > thresh
    utils.show_image(binary,'global thresh')
    return binary



def threshold_inversed_scikit(image):
    image_gray = color.rgb2gray(image)
    thresh = threshold_otsu(image_gray)
    binary = image_gray <= thresh
    utils.show_image(binary,'inverse thresh')
    return binary


def thresh_local(image):
    image_gray = color.rgb2gray(image)
    block_size =35
    local_thresh = threshold_local(image_gray,block_size,offset=10)
    binary_local= image_gray > local_thresh
    utils.show_image(binary_local,'local thresh')
    return binary_local  


def canny(image):
    image_gray= color.rgb2gray(image)
    edges = feature.canny(image_gray,sigma=3)
    utils.show_image(edges,'cannyImage')
    return edges

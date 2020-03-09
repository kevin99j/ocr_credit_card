import matplotlib.pyplot as plt
import cv2
from skimage.transform import rescale, resize



def show_image(image,title='Image',cmap_type='gray'):
    plt.imshow(image,cmap=cmap_type)
    plt.title(title)
    plt.axis('off')
    plt.show()


def show_image_cv(image,title):
    cv2.namedWindow(title, cv2.WINDOW_AUTOSIZE)
    cv2.imshow(title,image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def rescaled(image):
    return resize(image,(image.shape[0]//4,image.shape[1]//4),anti_aliasing=True)
import cv2



def upscale_image(image):
    width = 640
    height = 480
    dim=(width,height)
    rezised_image =cv2.resize(image,dim,interpolation=cv2.INTER_AREA)
    return rezised_image
import cv2
import pytesseract
import optimization as op
import filtering_scikit as fsc
import matplotlib as mpl
mpl.use('TkAgg')
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import utils as utils 
import resolution as rs


#img = mpimg.imread('assets/testR_02.png')
img = cv2.imread('assets/text13.png')
print(img.shape)
#img = rs.upscale_image(img)
img = utils.rescaled(img)
print(img.shape)
#img = rs.upscale_image(img)
#img_rotated = cv2.rotate(img,cv2.ROTATE_90_COUNTERCLOCKWISE)
#gray_image = op.get_grayscale(img)
#no_noise = op.remove_noise(gray_image)
#thresh = op.thresholding(no_noise)
#opening = op.opening(gray_image)
#canny = op.canny(gray_image)
custom_config= r'--oem --psm6 outputbase digits'


#utils.show_image_cv(thresh,'no noise thresh')

# scikit image processing

#thresh_local = fsc.thresh_local(img)
thresh = fsc.threshold_scikit(img)
inverse_thresh = fsc.threshold_inversed_scikit(img)
inverse_thresh = fsc.threshold_inversed_scikit(inverse_thresh)
#canny_image = fsc.canny(img)
canny_thresh = fsc.canny(inverse_thresh)


#resultG = pytesseract.image_to_string(img,config=custom_config ,lang='crspa')
resultT= pytesseract.image_to_string(inverse_thresh,config=custom_config,lang='crspa')
#resultO= pytesseract.image_to_string(canny_image,config=custom_config,lang='crspa')
resultC= pytesseract.image_to_string(canny_thresh,config=custom_config,lang='crspa')
#print('{}{}'.format('el resultado de grayscale es ',resultG))
print('{}{}'.format('el resultado de threshold es',resultT))
#print('{}{}'.format('el resultado de opening es',resultO))
print('{}{}'.format('el resultado de canny es',resultC)) 

 
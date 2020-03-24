import cv2
import pytesseract
import utils as ut


img = cv2.imread('assets/testR_02.jpg')


h,w,c = img.shape
boxes = pytesseract.image_to_boxes(img)

for b in boxes.splitlines():
    b = b.split(' ')
    img = cv2.rectangle(img,(int(b[1]), h-int(b[2])),(int(b[3]),h-int(b[4])),(0,255,0),2)

ut.show_image_cv(img,'boxes')
 
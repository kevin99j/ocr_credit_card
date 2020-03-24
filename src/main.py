import core.text_detection as text_detection  
import os 
import re

#ImagesPath = 'E:/IA/credit_card_ocr/assets/images/Cropped_images'
ImagesPath = 'E:/IA/credit_card_ocr/assets/images/docs'
ImagePath = 'E:/IA/credit_card_ocr/assets/images/Cropped_images/img4.jpeg'

def get_transformed_images():
    for filename in os.listdir(ImagesPath):
        if re.match('[A-ñ0-9]*.jpe?g',filename):
            text_detection.extract_text(os.path.join(ImagesPath,filename))




if __name__ == "__main__":
    get_transformed_images()
   #text_detection.extract_text(ImagePath)
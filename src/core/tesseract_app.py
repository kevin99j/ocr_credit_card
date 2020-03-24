import pytesseract


CONFIG = r'--oem --psm6 outputbase digits'


def get_image_text(image):
    return pytesseract.image_to_string(image)
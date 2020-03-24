from PIL import Image





def transform(image,formato):
    im = Image.open(image)
    im.save(formato)




transform('assets/testR_02.jpg','assets/testR_02.png')
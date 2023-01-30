from PIL import Image,ImageEnhance,ImageFilter
import os 
img1 = Image.open('dog1.jpg')
img1.show()
img1.save()
max - (250,250)
img1.thumbnail('dog1small.jpg')

for item in os.listdir():
    if item.endswith('.jpg'):
        image1 = Image.open(item)
        filename,extension=os.path.splitext(item)
        img1.save(f'{filename}.png')
en = ImageEnhance.Sharpness(img1)
en.enhance(0).save('dog2.jpg')
en = ImageEnhance.Color(img1)
en.enhance(2).save('dog3.jpg')
en = ImageEnhance.Brightness(img1)
en.enhance(3).save('dog4.jpg')

img1.filter(ImageFilter.GaussianBlur()).save('dog5.jpg')
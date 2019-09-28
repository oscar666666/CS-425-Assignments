from matplotlib import pyplot as plt
import numpy as np
from PIL import Image

rawData = open("rose.raw", 'rb').read()
imgSize = (256, 256)  # the image size
img = Image.frombytes('L', imgSize, rawData)
img.save("256x256.jpeg")  # can glsive any format you like .png

imgar = np.array(img)
print(imgar)
print(imgar.shape)

t_list =[]
for i in range(0, 256, 2):
    t_list.append(i)

#------------produce 128x128----------------------------
imgar = np.delete(imgar, t_list, 0)#remove every second row
imgar = np.delete(imgar, t_list, 1)#remove every second column
print(imgar.shape)
img = Image.fromarray(imgar)
img.save('128x128.png')


#------------produce 64x64----------------------------

imgar = np.delete(imgar, t_list, 0)#remove every second row
imgar = np.delete(imgar, t_list, 1)#remove every second column
print(imgar.shape)
img = Image.fromarray(imgar)
img.save('64x64.png')


#------------produce 32x32----------------------------

imgar = np.delete(imgar, t_list, 0)#remove every second row
imgar = np.delete(imgar, t_list, 1)#remove every second column
print(imgar.shape)
img = Image.fromarray(imgar)
img.save('32x32.png')


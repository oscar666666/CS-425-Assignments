from matplotlib import pyplot as plt
import numpy as np
from PIL import Image

rawData = open("rose.raw", 'rb').read()
imgSize = (256, 256)  # the image size
img = Image.frombytes('L', imgSize, rawData)
img.save("256x256.png")  # can glsive any format you like .png

imgar = np.array(img)
print(imgar.shape)

#------------produce shift 2 image----------------------------
shift2 = np.right_shift(imgar, 2)  
shift2 = np.left_shift(imgar, 2)  
img = Image.fromarray(shift2)
img.save('shift2.png')
np.array(shift2).tofile("shift2.raw")
#------------produce shift 3 image----------------------------
shift3 = np.right_shift(imgar, 3)  
shift3 = np.left_shift(imgar, 3)  
img = Image.fromarray(shift3)
img.save('shift3.png')
np.array(shift3).tofile("shift3.raw")


#------------produce shift 4 image----------------------------
shift4 = np.right_shift(imgar, 4)  
shift4 = np.left_shift(imgar, 4)  
img = Image.fromarray(shift4)
img.save('shift4.png')
np.array(shift4).tofile("shift4.raw")

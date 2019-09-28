from matplotlib import pyplot as plt
import numpy as np
from PIL import Image
import collections as collections
import cv2

rawData = open("rose.raw", 'rb').read()
imgSize = (256, 256)  # the image size
img = Image.frombytes('L', imgSize, rawData)
img.save("256x256.png")  # can glsive any format you like .png

imgar = np.array(img)
print(imgar.shape)

histogram = np.zeros((256,256))
histogram = histogram + 255
print(histogram)

unique_elements, counts_elements = np.unique(imgar, return_counts=True)
print("Frequency of unique values of the said array:")
print(np.asarray((unique_elements, counts_elements)))

print("--------------------------------------")
counts_elements = (counts_elements/5255*256).astype(int)
print("--------------------------------------")

for i in range(0, len(unique_elements)):
    #write 0 to the row has count number
    histogram[255-counts_elements[i]][unique_elements[i]]=0
    for k in range(0, counts_elements[i]):
        #write 0 to the rest rows
        histogram[255-k][unique_elements[i]]=0

img = Image.fromarray(histogram)
img = img.convert("L")
img.save('hist-raw-256x256.png')


'''
#-------------------test----------------------
im = cv2.imread('256x256.png')
# calculate mean value from RGB channels and flatten to 1D array
vals = im.mean(axis=2).flatten()
# plot histogram with 255 bins
b, bins, patches = plt.hist(vals, 255)
plt.xlim([0,255])
plt.show() 
'''
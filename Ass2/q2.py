from matplotlib import pyplot as plt
import numpy as np
from PIL import Image
import collections as collections
import cv2


def H1Filter(name):

    # --------------------fetch raw image----------------------------
    rawData = open(name+".raw", 'rb').read()
    imgSize = (256, 256)  # the image size
    img = Image.frombytes('L', imgSize, rawData)
    img.save(name+"original.png")  # can glsive any format you like .png

# -----------------save image to 2d array--------------------
    imgar = np.array(img)
    imgar_copy = imgar.copy()

    for l in range(1, 255, 1):
        for w in range(1, 255, 1):
            sum = 0
            for i in range(-1, 2, 1):
                for j in range(-1, 2, 1):
                    p = (imgar[l+i][w+j])
                    sum = sum + p
            sum = int(sum/9)
            imgar_copy[l][w] = sum
    print(imgar)
    print(imgar_copy)
    img = Image.fromarray(imgar_copy)
    img.save(name+ '-H1-filter.png')
    np.array(img).tofile(name+"-H1-filter.raw")


def H2Filter(name):

    # --------------------fetch raw image----------------------------
    rawData = open(name+".raw", 'rb').read()
    imgSize = (256, 256)  # the image size
    img = Image.frombytes('L', imgSize, rawData)
    img.save(name+"original.png")  # can glsive any format you like .png

# -----------------save image to 2d array--------------------
    imgar = np.array(img)
    imgar_copy2 = imgar.copy()
    H2 = np.array([
        [0.075, 0.125, 0.075],
        [0.125, 0.2, 0.125],
        [0.075, 0.125, 0.075]]
    )
    
    for l in range(1, 255, 1):
        for w in range(1, 255, 1):
            sum = 0
            for i in range(-1, 2, 1):
                for j in range(-1, 2, 1):
                    p = (imgar[l+i][w+j])
                    sum = sum + (p*H2[i+1][j+1])
            sum = int(sum)
            imgar_copy2[l][w] = sum
            
    print(imgar)
    print(imgar_copy2)
    img = Image.fromarray(imgar_copy2)
    img.save(name+ '-H2-filter.png')
    np.array(img).tofile(name+"-H2-filter.raw")


def main():

    H1Filter("testpattern")
    H2Filter("testpattern")

if __name__ == "__main__":
    # execute only if run as a script
    main()
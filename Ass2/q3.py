from matplotlib import pyplot as plt
import numpy as np
from PIL import Image
import collections as collections
import cv2


def MedianFilter(name):

    # --------------------fetch raw image----------------------------
    
    rawData = open(name+".raw", 'rb').read()
    imgSize = (256, 256)  # the image size
    img = Image.frombytes('L', imgSize, rawData)
    img.save(name+"original.png")  # can glsive any format you like .png
    '''
    im = cv2.imread("test.jpg",cv2.IMREAD_GRAYSCALE)
    '''
# -----------------save image to 2d array--------------------
    imgar = np.array(img)
    imgar_copy2 = imgar.copy()

    
    for l in range(1, 255, 1):
        for w in range(1, 255, 1):
            sum = []
            for i in range(-1, 2, 1):
                for j in range(-1, 2, 1):
                    sum.append(imgar[l+i][w+j])
                    
            sum.sort()
            #print(sum)
            imgar_copy2[l][w] = sum[4]
            
    img = Image.fromarray(imgar_copy2)
    img.save(name+ '-Median-filter.png')
    np.array(img).tofile(name+"-Median-filter.raw")

def main():

     MedianFilter("circuit")


if __name__ == "__main__":
    # execute only if run as a script
    main()
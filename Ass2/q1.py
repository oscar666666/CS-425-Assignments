from matplotlib import pyplot as plt
import numpy as np
from PIL import Image
import collections as collections
import cv2


def histogramEqualization(name):

    # --------------------fetch raw image----------------------------
    rawData = open(name+".raw", 'rb').read()
    imgSize = (256, 256)  # the image size
    img = Image.frombytes('L', imgSize, rawData)
    img.save(name+"original.png")  # can glsive any format you like .png

# -----------------save image to 2d array--------------------
    imgar = np.array(img)
    unique_elements, counts_elements = np.unique(imgar, return_counts=True)
    print("Frequency of unique values of the said array:")
    print(np.asarray((unique_elements, counts_elements)))
    print(counts_elements.size)
    H = counts_elements
    for i in range(1, 72, 1):
        H[i] = H[i]+ H[i-1]
    print(H)

    '''
    img = cv2.imread('ctoriginal.png',0)
    plt.hist(img.ravel(),256,[0,256]); plt.show()
    
    '''
#---------------------Useful variables------------------------
    K = 256
    for i in range(0, 256):
        for j in range(0, 256):
            index = np.where(unique_elements == imgar[i][j])
            imgar[i][j] = (H[index] * (K-1))/(256 * 256)

    img = Image.fromarray(imgar)
    img.save('imgar.png')
    np.array(img).tofile(name+"hist-raw-equalization.raw")

    '''
    img = cv2.imread('imgar.png',0)
    plt.hist(img.ravel(),256,[0,256]); plt.show()
    '''


def main():

     histogramEqualization("ct")


if __name__ == "__main__":
    # execute only if run as a script
    main()
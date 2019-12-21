from matplotlib import pyplot as plt
import numpy as np
from PIL import Image
import collections as collections
import cv2
import math

def SobelEdgeOperators(name):

    SobelX = np.array([
        [-1, 0, 1],
        [-2, 0, 2],
        [-1, 0, 1]]
    )
    SobelY = np.array([
        [-1, -2, -1],
        [0, 0, 0],
        [1, 2, 1]]
    )
    # --------------------fetch raw image----------------------------
    
    rawData = open(name+".raw", 'rb').read()
    imgSize = (560, 420)  # the image size (width, height)
    img = Image.frombytes('L', imgSize, rawData)
    img.save(name+"_original.png")  # can glsive any format you like .png
    '''
    im = cv2.imread("test.jpg",cv2.IMREAD_GRAYSCALE)
    '''
# -----------------save image to 2d array--------------------
    imgar = np.array(img)
    imgar_copy2 = imgar.copy()
    imgar_copy3 = imgar.copy()
    imgar_copy4 = imgar.copy()


    print(imgar.shape)
#-----------------------Calculate Sobel filter--------------------------
    for width in range(1, 559, 1):
        for height in range(1, 419, 1):
            sumx = 0
            sumy = 0
            sum = 0
            for i in range(-1, 2, 1):
                for j in range(-1, 2, 1):
                    p = (imgar[height+i][width+j])
                    sumx = sumx + (p*SobelX[i+1][j+1])
                    sumy = sumy + (p*SobelY[i+1][j+1])
            sum = int(abs(math.sqrt((sumx*sumx) + (sumy*sumy))))
            imgar_copy3[height][width] = int(abs(sumx))
            imgar_copy4[height][width] = int(abs(sumy))
            imgar_copy2[height][width] = sum
#----------------------set pixel to 0 if p < 128------------------------
    TE = 128
    imgar_copy5 = imgar_copy2.copy()
    for width in range(1, 559, 1):
        for height in range(1, 419, 1):
            p = (imgar_copy2[height][width])
            if(p<TE):
                imgar_copy5[height][width] = 0

    #-----------------output raw image--------------------

    img = Image.fromarray(imgar_copy2)
    img.save(name+ '-SobelEdgeOperator.png')
    np.array(img).tofile(name+"-SobelEdgeOperator.raw")

    img = Image.fromarray(imgar_copy3)
    img.save(name+ '-X-SobelEdgeOperator.png')
    np.array(img).tofile(name+"-X-SobelEdgeOperator.raw")

    img = Image.fromarray(imgar_copy4)
    img.save(name+ '-Y-SobelEdgeOperator.png')
    np.array(img).tofile(name+"-Y-SobelEdgeOperator.raw")

    img = Image.fromarray(imgar_copy5)
    img.save(name+ '-TE-SobelEdgeOperator.png')
    np.array(img).tofile(name+"-TE-SobelEdgeOperator.raw")




def main():

     SobelEdgeOperators("building")


if __name__ == "__main__":
    # execute only if run as a script
    main()
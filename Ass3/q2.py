import numpy as np
from PIL import Image

import math

def LaplacianSharpening(name):

    Hl = np.array([
        [0, 1, 0],
        [1, -4, 1],
        [0, 1, 0]]
    )

    # --------------------fetch raw image----------------------------
    
    rawData = open(name+".raw", 'rb').read()
    imgSize = (464, 528)  # the image size (width, height)
    img = Image.frombytes('L', imgSize, rawData)
    img.save(name+"_original.png")  # can glsive any format you like .png
    '''
    im = cv2.imread("test.jpg",cv2.IMREAD_GRAYSCALE)
    '''
# -----------------save image to 2d array--------------------
    imgar = np.array(img)
    imgar_copy2 = imgar.copy()
    imgar_copy3 = imgar.copy()

    w = 0.4

#-----------------------Calculate Laplacian--------------------------
    for width in range(1, 463, 1):
        for height in range(1, 527, 1):
            sum = 0
            for i in range(-1, 2, 1):
                for j in range(-1, 2, 1):
                    p = (imgar[height+i][width+j])

                    sum = sum + (p*Hl[i+1][j+1])
            
            imgar_copy2[height][width] = abs(sum)
            temp = imgar[height][width] - (w * sum)
            if (temp < 0):
                temp = 0
            if (temp > 255):
                temp = 255
            imgar_copy3[height][width] = int(temp)



    #-----------------output raw image--------------------
    img = Image.fromarray(imgar_copy2)
    img.save(name+ '-Laplacian.png')
    np.array(img).tofile(name+"-Laplacian.raw")

    img = Image.fromarray(imgar_copy3)
    img.save(name+ '-LaplacianSharpening.png')
    np.array(img).tofile(name+"-LaplacianSharpening.raw")





def main():

     LaplacianSharpening("moon")


if __name__ == "__main__":
    # execute only if run as a script
    main()
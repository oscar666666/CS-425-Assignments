from matplotlib import pyplot as plt
import numpy as np
from PIL import Image
import collections as collections
#import cv2

def imgtohist(name):

    # --------------------fetch raw image----------------------------
    rawData = open(name+".raw", 'rb').read()
    imgSize = (256, 256)  # the image size
    img = Image.frombytes('L', imgSize, rawData)
    #img.save("256x256.png")  # can glsive any format you like .png

# -----------------save image to 2d array--------------------
    imgar = np.array(img)
    print(imgar.shape)

# -----------------write all white pixcel to array--------------------
    histogram = np.zeros((256, 256))
    histogram = histogram + 255

# -----------------count histogram--------------------
    unique_elements, counts_elements = np.unique(imgar, return_counts=True)
    print("Frequency of unique values of the said array:")
    print(np.asarray((unique_elements, counts_elements)))

# -----------------normalize to at most value 255--------------------
    counts_elements = (counts_elements/5255*256).astype(int)

# ----------------------write 0 (black) to 2d array--------------------------
    for i in range(0, len(unique_elements)):
        # write 0 to the row has count number
        histogram[255-counts_elements[i]][unique_elements[i]] = 0
        for k in range(0, counts_elements[i]):
            # write 0 to the rest rows
          histogram[255-k][unique_elements[i]] = 0

# ----------------------out put to png--------------------------
    img = Image.fromarray(histogram)
    img = img.convert("L")
    img.save(name+'hist-raw-256x256.png')
    np.array(img).tofile(name+"hist-raw-256x256.raw")

# ---------------------------q2 image 1---------------------
def main():

    imgtohist("rose")
    imgtohist("shift2")#for shift 2 image
    imgtohist("shift3")
    imgtohist("shift4")

if __name__ == "__main__":
    # execute only if run as a script
    main()
from matplotlib import pyplot as plt
import numpy as np
from PIL import Image
import collections as collections
import cv2
import math
import cmath

def FFT_Row():
    I_list = []
    for i in range(0, 256, 1):
        I_list.append(i)
    for i in range(0, 256, 1):
        I_list[i] = reverseBits(i,8)
    print(I_list)

#https://www.geeksforgeeks.org/reverse-bits-positive-integer-number-python/
# Function to reverse bits of positive  
# integer number 
  
def reverseBits(num,bitSize): 
  
     # convert number into binary representation 
     # output will be like bin(10) = '0b10101' 
     binary = bin(num) 
  
     # skip first two characters of binary 
     # representation string and reverse 
     # remaining string and then append zeros 
     # after it. binary[-1:1:-1]  --> start 
     # from last character and reverse it until 
     # second last character from left 
     reverse = binary[-1:1:-1] 
     reverse = reverse + (bitSize - len(reverse))*'0'
  
     # converts reversed binary string into integer 
     return int(reverse,2) 

def FFT(name):

    # --------------------fetch raw image----------------------------
    
    rawData = open(name+".raw", 'rb').read()
    imgSize = (256, 256)  # the image size
    img = Image.frombytes('L', imgSize, rawData)
    img.save(name+"-original.png")  # can glsive any format you like .png

# -----------------save image to 2d array--------------------
    imgar = np.array(img)
    imgar_rearrange = imgar.copy()
    F1 = imgar.copy()
    F2 = imgar.copy()

#-----------------------Rearrange array elements--------------------------
    FFT_Row()
#-----------------------FFt--------------------------

    #creat a list of lists to do 1d fft on every row 
    A1 = []
    A1List = []
    for height in range(0, 256, 1):
        for width in range(0, 256, 1):
            A1.append(F2[height][width])
        A1List.append(A1)
        A1 = []

    #1d fft

    for height in range(0, 256, 1):
        A1List[height] = np.fft.fft(A1List[height])
    
    A1List = np.array(A1List)
    A1 = []
    A2List = []

    #creat a list of lists to do 1d fft on every column 
    for width in range(0, 256, 1):
        for height in range(0, 256, 1):
            A1.append(A1List[height][width])
        A2List.append(A1)
        A1 = []
    #1d fft
    for height in range(0, 256, 1):
        A2List[height] = np.fft.fft(A2List[height])
    #convert to mangnitude/spectrom
    A2List = np.array(A2List)
    A2List = A2List.transpose()
    for height in range(0, 256, 1):
        for width in range(0, 256, 1):
            F2[height][width] = int(np.real(cmath.sqrt(A2List[height][width].real**2 + A2List[height][width].imag**2)))
    
    #-----------------output raw image--------------------
    img = Image.fromarray(F2)
    img.save(name+ '-FFT-spectrom.png')
    np.array(img).tofile(name+"-FFT-spectrom.raw")

#------------------cv2 lib + shift 0 freq to center of the spectrum--------------
'''
    img3 = cv2.imread('car-original.png',0)
    f = np.fft.fft2(img3)
    fshift = np.fft.fftshift(f)
    magnitude_spectrum = 20*np.log(np.abs(fshift))

    plt.subplot(122),plt.imshow(magnitude_spectrum, cmap = 'gray')
    plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
    plt.show()
    '''

def main():

     FFT("car")


if __name__ == "__main__":
    # execute only if run as a script
    main()
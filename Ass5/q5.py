from matplotlib import pyplot as plt
import numpy as np
from PIL import Image
import collections as collections
import cv2
import math
import cmath

def FFT_Row(fft_row):
    fft_row1 = []
    I_list = []
    for i in range(0, 256, 1):
        I_list.append(i)
    for i in range(0, 256, 1):
        I_list[i] = reverseBits(i,8)
    #---store values in shuffled order
    for i in range(0, 256, 1):
        fft_row1.append(fft_row[I_list[i]])
    #-----fft-----------------
    M = 1
    j = int(256/2)
    n = int(math.log2(256))
    fft_row2 = []
    for i in range(0, n, 1):
        for k in range(0, j, 1):
            # Start of first sub-group
            i1 = 2 * k * M
            #Start of second sub-group
            i2 = ((2 * k) + 1) * M
            for u in range(0, M, 1):
                Wnu = math.e**((complex(0,-1)*2*math.pi*u)/2*M)
                #print(Wnu)
                fft_row2.append(0.5*(fft_row1[i1+u] + (fft_row1[i2+u] * Wnu)))
                
            for u in range(0, M, 1):
                Wnu = math.e**((complex(0,-1)*2*math.pi*u)/2*M)
                fft_row2.append(0.5*(fft_row1[i1+u] - (fft_row1[i2+u] * Wnu)))
        # Double the size of the sub-groups
        M = int(M*2)

        # Reduce number of sub-groups by half
        j = int(j/2)
    return fft_row2
    

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
#-----------------------FFt--------------------------

    #creat a list of lists to do 1d fft on every row 
    A1 = []
    A1List = []
    for height in range(0, 256, 1):
        for width in range(0, 256, 1):
            A1.append(complex(F2[height][width],0))
        A1List.append(A1)
        A1 = []

    #1d fft
    for height in range(0, 256, 1):
        A1List[height] = FFT_Row(A1List[height])
    A1List = np.array(A1List)
    A1 = []
    A2List = []
    #print(A1List)

    #creat a list of lists to do 1d fft on every column 
    for width in range(0, 256, 1):
        for height in range(0, 256, 1):
            A1.append(A1List[height][width])
        A2List.append(A1)
        A1 = []
    #1d fft
    for height in range(0, 256, 1):
        A2List[height] = FFT_Row(A2List[height])
    #convert to mangnitude/spectrom
    A2List = np.array(A2List)
    A2List = A2List.transpose()
    #print(A2List)
    for height in range(0, 256, 1):
        for width in range(0, 256, 1):
            F2[height][width] = int(np.real(cmath.sqrt(A2List[height][width].real**2 + A2List[height][width].imag**2)))
    
    #-----------------output raw image--------------------
    #print(F2)
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
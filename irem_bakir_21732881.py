# GMT-431
# FALL 20-21
#FINAL EXAM
#
#
#
# İREM BAKIR
# 21732881
# The first and second definitions are for question one.
#
# The third and fourth definitions are for question two.


import cv2                   #Libraries I used: opencv, numpy
import numpy as np
imgL = cv2.imread('im1.png', 0)         #read the image 1
imgR = cv2.imread('im2.png', 0)         #read the image 2

#QUESTION-1
    
window_size = 5
minDisp = -1
numDisp = 255 - minDisp
stereo = cv2.StereoSGBM_create(minDisparity=minDisp,
                               numDisparities=numDisp,
                               blockSize=window_size,
                               P1=8 * 3 * window_size**2,
                               P2=32 * 3 * window_size**2,
                               disp12MaxDiff=1,
                               uniquenessRatio=5,
                               speckleWindowSize=100,
                               speckleRange=1)


def Left2Right():           #definition for left image to right image
    disparity = stereo.compute(imgL, imgR).astype(np.float32) / 16.0
    cv2.imwrite('disparityL2R.png', disparity)

Left2Right()

### https://docs.opencv.org/3.4/d2/d85/classcv_1_1StereoSGBM.html
##According to the references I added,
#I changed the values within this framework and used the values
#that seemed most correct to me according to their output.


#QUESTION-2

disparity1 = cv2.imread('disparityL2R.png', 0)
groundTruth1 = cv2.imread('GTdisp_im1.png', 0)

# I introduced the images


def gtl2r():
    size = disparity1.shape
    height = size[0]
    print("Height of the image : " , height)
    width = size[1]
    print("Width of the image :  " , width)

    goodPixels = 0      #I have defined the correct pixels
    unknown = 0     #I have defined the wrong pixels

    for i in range(height):
        for j in range(width-numDisp):
            if groundTruth1[i, j+numDisp] != 0:         #I found non-zero values
                if abs(np.array(disparity1[i, j+numDisp].astype(np.float32))  
                       -np.array(groundTruth1[i, j+numDisp].astype(np.float32))) <= 1:
#  I subtracted the number of disparity value from the width value
# because the non-overlapping part in the disparity picture is equal
                    goodPixels += 1         #I added the found values to the correct pixel.
            if groundTruth1[i, j+numDisp] == 0:         #I found values equal to zero
                unknown += 1

    truePixels = (goodPixels / (((width-numDisp) * height) - unknown)) * 100
    wrongPixels = 100 - truePixels
    print('This disparity map is %{0:.2f} true'.format(truePixels))
    print('Percentage of different pixels %{0:.2f} '.format(wrongPixels))
    print("Unknown disparity values : " , unknown)

gtl2r()

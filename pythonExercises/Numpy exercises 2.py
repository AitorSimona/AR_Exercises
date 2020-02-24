import numpy as np 
import cv2 

# Exercise 1: Open an image maintaining its original color format and print its internal data type, its
# shape, its number of dimensions, and show it in a window.

def ex1():
    img = cv2.imread("vegetto.png", cv2.IMREAD_UNCHANGED)
    cv2.imshow("img", img)
    dimensions = img.shape
    print('Image Height       : ',img.shape[0])
    print('Image Width        : ',img.shape[1])
    print('Number of Channels : ',img.shape[2])
    print('Data type : ', type(img[0,0,0]))
    cv2.waitKey(0) 

# Exercise 2:Open an image maintaining its original color format, cast it to contain floating point
# values, convert all pixels to range [0, 1], and show the image in a window.

def ex2():
    img = cv2.imread("vegetto.png", cv2.IMREAD_UNCHANGED)
    img = np.float64(img)
    img = cv2.normalize(img, None,0,1, norm_type = cv2.NORM_MINMAX, dtype = cv2.CV_32F)
    cv2.imshow("image", img)
    cv2.waitKey(0) 

# Exercise 2:  Create a binary image (0s and 1s) from an image file and show it.

def ex3():
    img = cv2.imread("vegetto.png", cv2.IMREAD_LOAD_GDAL)
    cv2.imshow("yosha", img)
    cv2.waitKey(0) 

ex3()
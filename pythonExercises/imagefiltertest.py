import cv2
import numpy as np

def boxFilter(img):

    # Kernel definition
    ksize = 6       # kernel size
    krad = int(ksize/2) #kernel radius 
    krn = np.ones((ksize , ksize))
    krn = krn / krn.sum() # normalize kernel

    height, width, depth = img.shape
    
    frm = np.ones((height + krad*2,                   
     width + krad*2,
     depth))
    frm[krad: -krad, krad: -krad] = img

    #filteted image(output)
    filter = np.zeros(img.shape)
    for i in range (0, height):
        for j in range (0,width):

            b = (frm[i:i+ksize, j:j+ksize, 0] * krn).sum()
            g = (frm[i:i+ksize, j:j+ksize, 1] * krn).sum()
            r = (frm[i:i+ksize, j:j+ksize, 2] * krn).sum()
            filter[i,j] = (b,g,r)
    return filter

img = cv2.imread("vegetto.png", cv2.IMREAD_ANYCOLOR)
img = img / 255.0


filtered = boxFilter(img)

cv2.imshow("Original",img)
cv2.imshow("Filtered", filtered)
cv2.waitKey(0)
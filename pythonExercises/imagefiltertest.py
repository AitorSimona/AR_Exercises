import cv2
import numpy as np

def convolve(img, krn, ksize, krad):

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

            #filter[i,j] = (frm[i:i+ksize, j:j+ksize]*krn[:,:,np.newaxis]).sum(axis=(0,1))


    return filter

def convolvegrayscale(img, krn, ksize, krad):

    height, width = img.shape
    
    frm = np.ones((height + krad*2,                   
     width + krad*2))
    frm[krad: -krad, krad: -krad] = img

    #filteted image(output)
    filter = np.zeros(img.shape)
    for i in range (0, height):
        for j in range (0,width):

            g = (frm[i:i+ksize, j:j+ksize] * krn).sum()
            filter[i,j] = g

            #filter[i,j] = (frm[i:i+ksize, j:j+ksize]*krn[:,:,np.newaxis]).sum(axis=(0,1))


    return filter

def gaussianKernel(krad):

    # Create empty matrix
    ksize = krad * 2 + 1
    krn = np.zeros((ksize,ksize))
    sigma = krad/3

    # Fill kernel with Gaussian values
    for i in range(0, ksize):
        for j in range(0, ksize):
            d = np.sqrt((krad - i)**2 + (krad - j)**2)
            krn[i,j] = np.exp(-(d**2/(2.0*sigma**2)))
            # TODO: compute d
            # TODO: compute G(d)
    
    # Normalize kernel
    krn/= krn.sum()

    return krn


def boxFilter(img):

    # Kernel definition
    ksize = 6       # kernel size
    krad = int(ksize/2) #kernel radius 
    krn = np.ones((ksize , ksize))
    krn = krn / krn.sum() # normalize kernel

    return convolve(img, krn, ksize, krad)

def gaussianFilter(img):

    # Kernel definition
    ksize = 61      # kernel size
    krad = int(ksize/2) #kernel radius 
    krn = gaussianKernel(krad) # normalize kernel

    return convolve(img, krn, ksize, krad)

def sobelFilter(img):

    # Kernel definition
    ksize = 3      # kernel size
    krad = int(ksize/2) #kernel radius 
    krn = np.zeros((ksize,ksize))
    list = [[-1,0,1],[-2,0,2],[-1,0,1]]
    krn = np.array(list)
    krn2 = np.transpose(krn)
    print(krn)
    print(krn2)

    # Create the gradient in x and in y
    img_x = convolvegrayscale(img, krn, ksize, krad)
    img_y = convolvegrayscale(img, krn2, ksize, krad)

    # Use both 
    G = np.sqrt(img_x**2 + img_y**2)

    return G





img = cv2.imread("vegetto.png", cv2.IMREAD_GRAYSCALE)
img = img / 255.0

filtered = sobelFilter(img)
filtered = filtered/filtered.max()

cv2.imshow("Original",img)
cv2.imshow("Filtered", filtered)
cv2.waitKey(0)
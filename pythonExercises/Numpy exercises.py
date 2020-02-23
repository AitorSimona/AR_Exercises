import numpy as np 
import cv2 

# Exercise 1: Create a vector of 10 floats (zeros)

def ex1():
    arr = np.zeros(shape = (1,10))
    print(arr)

# Exercise 2: Create a vector of 10 float (zeros) whose 5th element is one

def ex2():
    arr = np.zeros(shape = (1,10))
    arr[0,4] = 1.0
    print(arr)

# Exercise 3: Create a vector of integers going from 10 to 49

def ex3():
    arr = np.arange(10, 50) # ints from 0 to 9
    print(arr)

# Exercise 4: Create a matrix of 3x3 floats going from 1 to 9

def ex4():        
    arr = np.arange(1,10)
    arr = arr.reshape(3, 3)
    print(arr)   

# Exercise 5: Create a matrix of 3x3 floats going from 1 to 9 and flip it horizontally

def ex5():
    arr = np.arange(1,10)
    arr = arr.reshape(3,3)
    arr = np.flip(arr,1)
    print(arr)   

# Exercise 6: Create a matrix of 3x3 floats going from 1 to 9 and flip it vertically

def ex6():
    arr = np.arange(1,10)
    arr = arr.reshape(3,3)
    arr = np.flip(arr,0)
    print(arr) 

# Exercise 7: Create a 3x3 identity matrix

def ex7():
    arr = np.identity(3)
    print(arr)

# Exercise 8: Create a 3x3 matrix of random values

def ex8():
    arr = np.random.random_sample((3, 3)) # 2x3 array of random floats from 0 to 1
    print(arr)

# Exercise 9: Create a random vector of 10 numbers and compute the mean value

def ex9():
    arr = np.random.randint(0,10,11)
    avg = arr.mean()
    print(arr)
    print(avg)

# Exercise 10: Create a 10x10 array of zeros surrounded/framed by ones

def ex10():
    arr = np.ones((5,5))
    arr[1:-1, 1:-1] = 0
    print(arr)

# Exercise 11:  Create a 5x5 matrix of rows from 1 to 5

def ex11():
    arr = np.zeros(shape = (5,5))
    arr[:, :] = np.arange(1,6)
    print(arr)

# Exercise 12:  Create an array of 9 random integers and reshape it to a 3x3 matrix of floats

def ex12():
    arr = np.random.randint(0, 100, 9)
    arr = arr.reshape(3,3)
    print(arr)

# Exercise 13:  Create a 5x5 matrix of random values and subtract its average from it

def ex13():
    arr = np.random.randint(0, 100, 25)
    arr = np.float64(arr)
    arr = arr.reshape(5,5)
    avg = arr.mean()
    arr -= avg
    print(avg)
    print(arr)

# Exercise 14:  Create a 5x5 matrix of random values and subtract the average of each row to each row

def ex14():
    arr = np.random.randint(0, 100, 25)
    arr = np.float64(arr)
    arr = arr.reshape(5,5)
    avg = np.zeros(shape=(1, 5))
    arr -= avg
    print(avg)
    print(arr)

#14 is not finished!!

# Exercise 15: Create an array of 5x5 random values and return the value that is closer to 0.5

def ex15():
    arr = np.random.uniform(0.0,1.0,(5,5))
    index = np.absolute(arr-0.5).argmin()
    arr = arr.flatten()
    print(arr[index])


# Exercise 16: . Make a 3x3 matrix of random numbers from 0 to 10 and count how many of them are > 5

def ex16():
    arr = np.random.randint(0,10,(3,3))
    print(arr)
    print(arr > 5)
    result = arr[arr>5]
    print(result)
    print(len(result))

# Exercise 17:  Create a horizontal gradient image of 64x64 that goes from black to white

def ex17():
    img = np.zeros((64,64))
    grad = np.arange(0.0,1.0,1.0/64.0)
    img = img + grad
    cv2.imshow("image", img)
    cv2.waitKey(0)

# Exercise 18: Create a vertical gradient image of 64x64 that goes from black to white

def ex18():
    img = np.zeros((64,64))
    grad = np.arange(0.0,1.0,1.0/64.0)
    grad = grad.reshape((64,1))
    img = img + grad
    cv2.imshow("image", img)
    cv2.waitKey(0)

# Exercise 19:Create a 3-component white image of 64x64 pixels and set the blue component to zero
# (the result should be yellow)

def ex19():
    img = 255 * np.ones((64,64,3), np.uint8)
    img[:, :, 0] = 0.0 
    cv2.imshow("image", img)
    cv2.waitKey(0)

# Exercise 20: Create a 3-component white image of 64x64 pixels, set the blue component of the
# top-left part to zero (the result should be yellow) and the red component of the
# bottom-right part to zero (the result should be cyan

def ex20(): 
    img = 255 * np.ones((64,64,3), np.uint8)
    img[:32, :32, 0] = 0.0 
    img[32:, 32:, 2] = 0.0 
    cv2.imshow("image", img)
    cv2.waitKey(0)

# Exercise 21: Open an image and insert black horizontal scan lines at 50%

def ex21():
    img = cv2.imread("vegetto.png", cv2.IMREAD_ANYCOLOR)
    img[::2, :] = 0.0
    cv2.imshow("image", img)
    cv2.waitKey(0)    

# Exercise 22: Open an image and insert black vertical scan lines at 50%

def ex22():
    img = cv2.imread("vegetto.png", cv2.IMREAD_ANYCOLOR)
    img[:, ::2] = 0.0
    cv2.imshow("image", img)
    cv2.waitKey(0)    

# Exercise 23: Open an image, convert it to float64, normalize it, darken it 50%, and show it
def ex23():
    img = cv2.imread("vegetto.png", cv2.IMREAD_ANYCOLOR)
    # normalize it by diving between mas (find max)
    img[:, ::2] = (img[:, ::2]/2)
    cv2.imshow("image", img)
    cv2.waitKey(0) 

ex23()

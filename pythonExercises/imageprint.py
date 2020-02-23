import cv2
import numpy

img = cv2.imread("vegetto.png",cv2.IMREAD_ANYCOLOR)
cv2.imshow('Vegetto', img)

k = cv2.waitKey(0)

if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('vegetto-show.png', img)
    cv2.destroyAllWindows()


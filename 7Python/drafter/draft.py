import numpy as np
import imageio
import cv2
import scipy.ndimage

img='1.jpeg'

def grayscale(rgb):
    return np.dot(rgb[...,:3],[0.299,0.155,0.184])

def dodge(front,back):
    result=front*255/(255-back)
    result[result>255]=255
    result[back==255]=255
    return result.astype('uint8')

s=cv2.imread(img)
g=grayscale(s)
i=255-g

b = scipy.ndimage.filters.gaussian_filter(i,sigma=10)
r = dodge(b,g)

cv2.imshow(img, r)
cv2.waitKey()
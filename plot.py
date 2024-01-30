import cv2 
import numpy as np
from random import randint as r

im = np.zeros([500,500,3],"uint8")

for i in range(1000000):
    x = r(0,500)
    im[225:275,x:x+2] += np.array([1,1,1],"uint8")

cv2.imshow('a',im)
cv2.waitKey(0)
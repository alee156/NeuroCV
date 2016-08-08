import cv2
import numpy as np

img = cv2.imread('Fear199.png',0)
equ = cv2.equalizeHist(img)
res = np.hstack((img,equ)) #stacking images side-by-side
cv2.imwrite('Fear199eq.png',res)

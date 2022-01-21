import math
import numpy as np
import cv2
image = cv2.imread('C:\\Users\\karthik\\Pictures\\water.jpg')
m,n,v = image.shape
gray_image = np.zeros((m,n),np.uint8)
image_onezeroes = np.zeros((m,n),np.uint8)
image_onezeroes2 = np.zeros((m,n),np.uint8)
print(m,n,v)
dummy = 0
for i in range(m):
    for j in range(n):
        for k in range(v):
            dummy = dummy + image[i][j][k]
        gray_image[i][j] = math.floor(dummy/3)
        dummy = 0
for t in range(m):
    for u in range(n):
        image_onezeroes[t][u] = (gray_image[t][u])/255

print("color image pixels")
print(image) 
print("gray image pixels")  
print(gray_image)
print("one/zero image pixels")
print(image_onezeroes)


cv2.imshow("original",image)
cv2.waitKey(0)
cv2.imshow('gray',gray_image)
cv2.waitKey(0)
cv2.imshow('zeroesones',image_onezeroes)
cv2.waitKey(0)
cv2.imshow('grayimage + zeroesoneimage ',gray_image + image_onezeroes)
cv2.waitKey(0)
cv2.imshow('grayimage + 20 ',gray_image + 20)
cv2.waitKey(0)
cv2.destroyAllWindows()
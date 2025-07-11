import cv2
import matplotlib.pyplot as plt
img=cv2.imread('C:\Users\patet\Downloads\opencv-4.x.zip\opencv-4.x\samples\data\lena.jpg',0)
img=cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
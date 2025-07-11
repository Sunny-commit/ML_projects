import cv2
img=cv2.imread('lena.jpg',0)
print(img)
cv2.imshow('image',img)
cv2.waitkey(5000)
cv2.destroyAllWindow()
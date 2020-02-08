#install -> pip install opencv-python 
import cv2
img=cv2.imread("3.1 galaxy.jpg.jpg",0)
print(type(img))
print(img)
print(img.shape)
print(img.ndim)
cv2.imshow("Galaxy",img)
cv2.waitKey(2000)
cv2.destroy

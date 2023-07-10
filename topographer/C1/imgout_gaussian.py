import cv2
import numpy

img = cv2.imread("topographer\C1\data\IMG20221012220608.jpg")

# def gaus_blur(image, kernel_size):
   
# apply guassian blur on src image
image_blur = cv2.GaussianBlur(img,(7,7),cv2.BORDER_DEFAULT)

# display input and output image
cv2.imshow("Gaussian Smoothing",numpy.hstack((img, image_blur)))
cv2.waitKey(0) # waits until a key is pressed
cv2.imshow("op", image_blur)
cv2.waitKey(0)
# print(image_crop.shape)
# Const path
cv2.imwrite("topographer\C1\data\op\output_blur.jpg", image_blur)

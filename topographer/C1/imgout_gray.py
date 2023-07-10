import cv2
#use standards defined in doc
#def grayscale():
image = cv2.imread('topographer\C1\data\IMG20221012220608.jpg')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
print(gray_image)
cv2.imshow('grayscale', gray_image)
# cv2.waitKey(0)
cv2.imwrite(r"./topographer/C1/output_gray.jpg", gray_image)


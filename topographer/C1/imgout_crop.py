import cv2
import numpy as np
import matplotlib
# from .mouse_center import on_mouse_center

# Load an image file
img = cv2.imread("topographer\C1\data\IMG20221012220608.jpg")
# Display the image on screen
# cv2.imshow("op",img)
cv2.waitKey(0)

def crop_around_center(image, crop_dims: int, center = cv2.EVENT_LBUTTONDOWN):

    # if center is None:
    #     height, width = image.shape[:2]
    #     c_y_min, c_x_min = height // 2 - crop_dims // 2, width // 2 - crop_dims // 2
    #     c_y_max, c_x_max = height // 2 + crop_dims // 2, width // 2 + crop_dims // 2
    #     image_crop = image[c_y_min:c_y_max, c_x_min:c_x_max]
    # else:
    #     # centerX, centerY = center
    #     centerX, centerY = cv2.EVENT_LBUTTONDOWN
    #     c_y_min, c_x_min = centerY - crop_dims // 2, centerX - crop_dims // 2
    #     c_y_max, c_x_max = centerY + crop_dims // 2, centerX + crop_dims // 2
    #     image_crop = image[c_y_min:c_y_max, c_x_min:c_x_max]

    centerX, centerY = cv2.EVENT_LBUTTONDOWN
    c_y_min, c_x_min = centerY - crop_dims // 2, centerX - crop_dims // 2
    c_y_max, c_x_max = centerY + crop_dims // 2, centerX + crop_dims // 2
    image_crop = image[c_y_min:c_y_max, c_x_min:c_x_max]

    cv2.imshow("op", image_crop)
    cv2.waitKey(0)
    # print(image_crop.shape)
    # Const path
    cv2.imwrite("topographer\C1\data\op\output.jpg", image_crop)

crop_around_center(img, 1000)



# Get the height and width of the image
# height, width = img.shape[:2]

# # Write image back to storage
# cv2.imwrite(output_folder + "/" + image_name + "/" + image_name + "crop.png", image_edge_inv)



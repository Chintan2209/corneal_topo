import cv2

# Set the crop size
crop_size = 800

def on_mouse_click(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f"Selected point: ({x}, {y})")
        crop_image_around_point(img, (x, y), crop_size)

def crop_image_around_point(img, point, crop_size):
    x, y = point
    crop_half_size = crop_size // 2
    cropped_img = img[y-crop_half_size:y+crop_half_size, x-crop_half_size:x+crop_half_size]
    cv2.imshow("Cropped Image", cropped_img)
    cv2.waitKey(0)

# Load an image from the file system
img = cv2.imread("topographer\C1\data\IMG20221012220608.jpg")
# img = cv2.resize(img, (540, 720)) 
# Display the image on the screen
cv2.namedWindow("Resized_Window", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Resized_Window", 810, 1080)
cv2.imshow("Resized_Window", img)

# Register the mouse click callback function
cv2.setMouseCallback("Resized_Window", on_mouse_click)

# Wait for a key press
cv2.waitKey(0)

# Set the crop size
crop_size = 1000

# Close all windows
cv2.destroyAllWindows()

import cv2
import numpy as np

class CircleDetector:
    def __init__(self, image_path):
        self.image_path = image_path
        self.image = None
        self.gray = None
        self.circles = None

    def load_image(self):
        self.image = cv2.imread(self.image_path)

    def convert_to_gray(self):
        self.gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)

    def detect_circles(self):
        self.circles = cv2.HoughCircles(self.gray, cv2.HOUGH_GRADIENT, 2.0, 600, minRadius = 50, maxRadius = 500)

    def draw_circles(self):
        if self.circles is not None:
            self.circles = np.round(self.circles[0, :]).astype("int")
            for (x, y, r) in self.circles:
                cv2.circle(self.image, (x, y), r, (0, 255, 0), 4)

    def show_image(self):
        cv2.namedWindow("Resized_Window", cv2.WINDOW_NORMAL)
        cv2.resizeWindow("Resized_Window", 810, 1080)
        cv2.imshow("Resized_Window", self.image)
        # cv2.imshow('blur', self.encImg)
        cv2.waitKey(0)    

# Example usage:
detector = CircleDetector('topographer\C1\output_enhance.jpg')

detector.load_image()
detector.convert_to_gray()
detector.detect_circles()
# detector.draw_circles()
detector.show_image()

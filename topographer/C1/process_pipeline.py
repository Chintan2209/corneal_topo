import cv2
import numpy as np
from enhance_img import image_enhance
class image_pipe:
    def __init__(self, fileName: str):
        self.iniImage = cv2.imread(fileName) 
        self.grayImg = self.gray_image()
        self.blurImg = self.blur_image()
        self.encImg = self.enhance_img()
        pass

    def gray_image(self):
        return cv2.cvtColor(self.iniImage, cv2.COLOR_BGR2GRAY)
    
    def blur_image(self):
        return cv2.GaussianBlur(self.grayImg, (5, 5), 0)
    
    def show_image(self):
        cv2.namedWindow("Resized_Window", cv2.WINDOW_NORMAL)
        cv2.resizeWindow("Resized_Window", 810, 1080)
        cv2.imshow("Resized_Window", self.encImg)
        # cv2.imshow('blur', self.encImg)
        cv2.waitKey(0)

    def writeImage(self):
        cv2.imwrite(r'./topographer/C1/output_enhance.jpg',self.encImg)

    def hough_transform(self,ups=1):	
        img= self.encImg
        orig = img.copy()
        pt0=0                                                           
        pt1=0                                                           
        #detected_circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1.0, 15, param1 = 55, param2 = 25, minRadius = 10*ups, maxRadius = 20*ups)
        detected_circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 2.0, 600, minRadius = 100*ups, maxRadius = 150*ups)
        if detected_circles is not None:                                
                # Convert the circle parameters a, b and r to integers. 
                detected_circles = np.uint16(np.around(detected_circles))
                                                                        
                for pt in detected_circles[0, :]:                       
                        a, b, r = pt[0], pt[1], pt[2]                   
                        pt0 = a                                         
                        pt1 = b                                         
                        print('Center detected:', a,b)                                               
                        # Draw the circumference of the circle.         
                        cv2.circle(orig, (a, b), r, (100, 255, 0), 2)   
                        break                                           
        #plt.figure()                                                    
        #plt.imshow(orig)                                                
        #plt.show()                                                      
        return pt0,pt1

    def draw_circles(self):
        if self.circles is not None:
            self.circles = np.round(self.circles[0, :]).astype("int")
            for (x, y, r) in self.circles:
                cv2.circle(self.image, (x, y), r, (0, 255, 0), 4)

    def enhance_img(self,downsample=False):
        rows,cols = np.shape(self.blurImg)
            
        aspect_ratio = np.double(rows)/np.double(cols)
        new_rows, new_cols = rows, cols

        if downsample == True:
            new_rows = 350
            new_cols = new_rows/aspect_ratio

        img = cv2.resize(self.blurImg,(np.int(new_cols),np.int(new_rows)))
        enhanced_img = image_enhance.image_enhance(img)
        enhanced_img = enhanced_img.astype(np.uint8)
        enhanced_img = cv2.resize(enhanced_img, (cols, rows), interpolation=cv2.INTER_LINEAR);
        enhanced_img = 255*enhanced_img
        return enhanced_img
        # print(enc_img)
        # return enhance_img.enhance_image(self.blurImg)
    

    

img = image_pipe('topographer\C1\data\IMG20221012220608.jpg')
print(img.hough_transform())
img.show_image()
img.writeImage()

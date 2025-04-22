"""
    Date: Sun-29-Sept-2024

    This episode demonstrates the use of Template Marching also called
    Object Detection.
    Template Marching basically means detecting an object or template image
    in another image.

    Here, the ball and shoe images are used as the template images.
    Also, it is important that the template images should be about the
    same size as that similar feature in the actual image.

    Note that not all the methods work correctly, hence why they are tested like in this
    tutorial 
"""

import cv2
import numpy as np


def main():
    #   0 for grayscale
    img = cv2.resize(cv2.imread("resources/images/soccer_practice.jpg", 0), (0, 0), fx=0.6, fy=0.6)
    # template = cv2.resize(cv2.imread("resources/images/ball.png", 0), (0, 0), fx=0.6, fy=0.6)
    template = cv2.resize(cv2.imread("resources/images/shoe.png", 0), (0, 0), fx=0.6, fy=0.6)


    # the shape of the grayscale image has no channel values.
    #   height, width is no. of rows, no. of columns
    height, width = template.shape
    
    #   Here are the methods for template marching
    """
        Each of these methods do similar things, or rather produce the same
        The point of so many methods is to test them. The method that
        gives the best result will continue to be used.
    """
    methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR,
               cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]
               
    for count, method in enumerate(methods):
        print("Method: {}".format(count + 1))
        img_copy = img.copy()
        #   template marching
        """
            It uses the Convolution algorithm
            the template is slid width-wise along the image
            and then a 2D resulting array of how well each region
            of the image matches the template, is created.

            The result will be
            (W - w + 1, H - h + 1)
            W, H = width and Height of main image
            w, h = width and hi

            The format:
            Image Array:
                [[255, 255, 255, 255],
                 [255, 255, 255, 255],
                 [255, 255, 255, 255],
                 [255, 255, 255, 255]
                ]
            Template Array:
                [[255, 255],
                 [255, 255]
                ]
            
            As the template array is moved over the image along its width
            starting from the top, it checks if the template array at that region
            matches the image
            If it does, here is how the *result* looks like:

            #   The template moves alongt the row; depending on the height
            #   the number of elements per row changes
            #   But the value that shows how much that region in the image matches the template
            #   is what populates this result array
            [[1, 0.2, 0.7],  #   A row
             [0.5, 0.1, 0.9]
            ] 
            Now, there is probably a threshold, i.e., for example
            if the value is > 0.7, it matches

            Afterward, the values that indicate a match, based on their position,
            in the result array, can be used to get the original postion of that area in the base image
            Hence the template match in the base image is gotten. 
        """
        result = cv2.matchTemplate(img_copy, template, method)
        #   The `minMaxLoc()` returns the min and max values as well
        #   as their locations in the array  
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

        print("Min: {}, Max: {}".format(min_loc, max_loc))
        #   Then draw a rectangle where the locations are in the base image
        
        #   When the method used is any of these two, the minimum location value
        #   should be used as it works the best then.
        #   But if any of the other 4, the max location value should be used.
        if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
            location = min_loc
        else:
            location = max_loc
        
        #   Because location is the top left corner of the image
        #   and the size of the feature being searched for in the base
        #   image is same as the templat, get the bottom right corner
        #   by adding the width and height appropriately
        bottom_right = (location[0] + width, location[1] + height)
        cv2.rectangle(img_copy, location, bottom_right, 255, 5)
        cv2.imshow("Object Detection", img_copy)
        cv2.waitKey(0)
        cv2.destroyAllWindows()



if __name__ == "__main__":
    main()
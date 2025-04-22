"""
    Date: sat-28-Sept-2024

    Demonstration of one of various algorithms openCV provides
    such as algorithms to detect corners in images.

    Here, the corners of the chessboard image are marked.
    And lines are drawn to cover various of them.
"""

import cv2
import numpy as np



def main():
    """
        Before running the algorithm to detect corners, the image
        has to be converted to gray as it is easier
        to do such operations on gray images.

        The algorithm is the Shi-Tomasi Corner Detector & Good Features to Track
    """
    img = cv2.imread("resources/images/chessboard.png")
    img = cv2.resize(img, (0, 0), fx=0.55, fy=0.55)   #   resize proportionally
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


    """
        args:
            1.  image
            2.  number of *best* corners to return in result image
            3.  Minimum quality for corners. value from 0 - 1.
                the smaller the number, the algorithm would return corners
                that its not very sure are corners.
                But the larger it is, the algorithm returns corners that
                it is more certain are corners.
                Start from 0.01
            4.  Minimum Euclidean distance between corners that are returned.
                It ensures that the corners returned are at least this minimum distance
                apart from one other.
    """
    #   This gives the array of location of the corners
    img_with_corners = cv2.goodFeaturesToTrack(gray_img, 100, 0.01, 10)
    # print(img_with_corners)
    #   Now, convert the corners pos data into integers because they are returned as floats
    #   It is converted to int because they are to be used to draw the points that mark the corners

    img_with_corners = np.intc(img_with_corners)

    """
        This is how the data is:
            [
                [[434 433]]
                [[324 324]]
                ...

            ]
    """
    #   So they need to be decomposed to get their positions
    #   then circles are drawn at their positions
    for corner in img_with_corners:
        """
           The `.ravel()` method flattens an array.
           so it changes something like this [[1, 2], [2, 2]] -> [1, 2, 2, 1]
           hence it changes the below likewise
        """
        x, y = corner.ravel()
        #   Now draw the corner as a circle
        cv2.circle(img, (x, y), 5, (0, 255, 255), -1)

    #   Draw lines that connect each corner to every other corner
    for i in range(len(img_with_corners)):
        for j in range(i + 1, len(img_with_corners)):
            """ 
               Because they have not yet been `ravel()`ed, just
               use index 0 to get the value
               img_with_corners = [
                                    [[233 322]]
                                        ...
                                   ]
               img_with_corners[i=0] = [[233 322]]
               E.g. img_with_corners[i=0][0] = [233 322] 
               tuple(img_with_corners[i=0][0]) converts to tuple
               to be used in cv2.line() method
            """
            corner1 = tuple(img_with_corners[i][0])
            corner2 = tuple(img_with_corners[j][0])
            #   this returns a list but the color argument needs to be
            #   transformed to a tuple/
            #   `np.random.randint` returns a 32 or 64-bit integer
            #   but only an 8-bit integer is required here
            #   so convert them using the lambda expression
            color = tuple(map(lambda x: int(x), np.random.randint(0, 255, size=3)))
            cv2.line(img, corner1, corner2, color, 1)

    cv2.imshow("Corner Detection", img)

    cv2.waitKey(0)

    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
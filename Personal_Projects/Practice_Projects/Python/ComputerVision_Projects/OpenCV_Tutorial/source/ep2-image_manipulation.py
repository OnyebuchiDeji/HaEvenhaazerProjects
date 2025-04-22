"""
    Date: Sat-27-Sept-2024

    this episode covers various image manipulations.
    E.g. copying a part of one image to another part of that same image.
    
    Even the rotating of an image is done by manipulating the numpy array
    that represents that image.
"""

import cv2
import random

def resize_image(img):
    #   Resize but in a more uniformly scalable way
    #   by using functions to modify the width and height
    #   This method can maintain the aspect ratio of the image.
    return cv2.resize(img, (0, 0), fx = 0.8, fy = 0.8)


def EG1(img):
    """

        If the channel mode is BGR, then the pixels'color channels
        are blue, green, red, respectively --> [12, 64, 128]
        [
            [[0, 0, 0], [255, 255, 255]],
            [[0, 125, 0], [255, 255, 0]]
        ]

        Hence images are modified by modifying this array that represents them
    """
    print(type(img))

    #   The shape tells the no. of rows, no. of columns, and no. of color channels
    print(img.shape)

def EG2_manipulating_img_pixels(img):
    #   Using slice
    # print(img[257][45:400]
    #   img.shape() returns the row_num, column_num, and color_channels
    for i in range(100):
        for j in range(img.shape[1]):
            img[i][j] = [random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)]
            
def EG3_copy_part_test(img):
    """

       Using the slice operator,
       choose the columns and rows of pixel data you want to cut out from the
       original image.
       It copies the a small area of the pixels from the image, 
       into `image_part`
       
       Now, remember that each row must have the same number of columns
       of pixel data, the number equal to the image's width.
       The number of rows corresponds to the image's height.

    """
    print("Image Array Rows, Columns, and Stride: ", img.shape)
    max_rows = img.shape[0] 
    max_cols = img.shape[1]

    print("Max Rows: ", max_rows)
    print("Max Cols: ", max_cols)
    
    """
        Note! Doing this correct way:
            `img[0:max_rows, 0:max_cols]`
        is not the same as:
            `ìmg[0:max_rows][0:max_cols]`
        
        The first is the right way to affect the 2D numpy array
        by using the slice operator to get the sub-array
        ranging from [0:max_rows] for the outer array
        and ranging from [0:max_cols] for the inner.
        Hence this effectively crops the image

        But the second is getting the pixels from [0:max_rows][o_max_cols]
        but not 
    """
    image_part = img[0:max_rows, 0:max_cols]
    image_part_false = img[0:max_rows][0:max_cols]
    print("Image Right Way Size: ", image_part.size)
    print("Image Right Way Shape: ", image_part.shape)
    print("Image Wrong Way Size: ", image_part_false.size)
    print("Image Wrong Way Shape: ", image_part_false.shape)

    #   Then here, a region in the actual image is selected
    #   and the pixels are replaced with the pixel patch just copied
    return image_part

def crop_part(img, x, y, crop_width, crop_height):
    return img[y:crop_height, x:crop_width]

def paste_crop(img, img_crop, target_xywh: tuple[int, int, int, int]):
    row_start = target_xywh[1]
    row_end = target_xywh[1] + target_xywh[3]
    col_start = target_xywh[0]
    col_end = target_xywh[0] + target_xywh[2]
    img[row_start:row_end, col_start:col_end] = img_crop
    return img


def main():
    #   This is a numpy array

    img = cv2.imread("resources/images/2004000.jpg", 1)
    img = resize_image(img)

    # EG2_manipulating_img_pixels(img)
    # img = EG3_copy_part_test(img)

    img_crop = crop_part(img, 0, 0, 200, 200)
    print("Crop Part Shape (Height, Width) == (Rows, Cols): ", img_crop.shape)

    ##  The width and height of the target area where the crop
    ##  is to be pasted must be the same as that of the crop itself
    img = paste_crop(img, img_crop, (100, 100, img_crop.shape[1], img_crop.shape[0]))

    cv2.imshow("Image", img)

    cv2.waitKey(0)
    #   It destroys all
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()


"""
    The members of a numpy array, from print(dir(img))
    ['T', '__abs__', '__add__', '__and__', '__array__', '__array_finalize__',
    '__array_function__', '__array_interface__', '__array_namespace__', '__array_priority__',
        '__array_struct__', '__array_ufunc__', '__array_wrap__', '__bool__', '__buffer__',
    '__class__', '__class_getitem__', '__complex__', '__contains__', '__copy__', '__deepcopy__',
    '__delattr__', '__delitem__', '__dir__', '__divmod__', '__dlpack__', '__dlpack_device__',
    '__doc__', '__eq__', '__float__', '__floordiv__', '__format__', '__ge__',
    '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__iadd__',
    '__iand__', '__ifloordiv__', '__ilshift__', '__imatmul__', '__imod__', '__imul__', '__index__',
    '__init__', '__init_subclass__', '__int__', '__invert__', '__ior__', '__ipow__', '__irshift__',
    '__isub__', '__iter__', '__itruediv__', '__ixor__', '__le__', '__len__', '__lshift__', '__lt__',
    '__matmul__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__',
    '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__',
    '__rfloordiv__', '__rlshift__', '__rmatmul__', '__rmod__', '__rmul__', '__ror__', '__rpow__',
    '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__setitem__',
    '__setstate__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__xor__',
    'all', 'any', 'argmax', 'argmin', 'argpartition', 'argsort', 'astype', 'base', 'byteswap',
    'choose', 'clip', 'compress', 'conj', 'conjugate', 'copy', 'ctypes', 'cumprod', 'cumsum',
    'data', 'device', 'diagonal', 'dot', 'dtype', 'dump', 'dumps', 'fill', 'flags', 'flat',
    'flatten', 'getfield', 'imag', 'item', 'itemset', 'itemsize', 'mT', 'max', 'mean', 'min',
    'nbytes', 'ndim', 'newbyteorder', 'nonzero', 'partition', 'prod', 'ptp', 'put', 'ravel',
    'real', 'repeat', 'reshape', 'resize', 'round', 'searchsorted', 'setfield', 'setflags',
    'shape', 'size', 'sort', 'squeeze', 'std', 'strides', 'sum', 'swapaxes', 'take', 'to_device',
    'tobytes', 'tofile', 'tolist', 'tostring', 'trace', 'transpose', 'var', 'view']
"""
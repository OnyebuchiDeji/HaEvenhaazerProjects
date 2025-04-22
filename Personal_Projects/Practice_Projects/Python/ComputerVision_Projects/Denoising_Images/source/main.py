"""
    Fri-04-Oct-2024
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt


"""
    Uses These Filter:
        GaussianBlur
        MedianBlur
        BilateralFilter 
"""
def denoise_image(image_path):
    noisy_image = cv2.imread(image_path)
    noisy_image_rgb = cv2.cvtColor(noisy_image, cv2.COLOR_BGR2RGB)

    """
        GaussianBlur: takes the weighted average of the surrounding pixels to determine
        the value of the surrrounded pixel. Closer pixels have more influence.

        MedianBlur: takes the mean value of all the pixels within the kernel area

        BilateralFilter: It reduces the noise while keeping the pixel's edges sharp by considering
        the number of neighboring pixels as well of the distance between the pixels and their color differences

    """
    #   the tuple is the Kernel Size: the size of the area to be considered to take
    #   the weighted average from
    gaussian_denoised_img = cv2.GaussianBlur(noisy_image, (5, 5), 0)
    gaussian_denoised_img_rgb = cv2.cvtColor(gaussian_denoised_img, cv2.COLOR_BGR2RGB)

    median_denoised_img = cv2.medianBlur(noisy_image, 5)
    median_denoised_img_rgb = cv2.cvtColor(median_denoised_img, cv2.COLOR_BGR2RGB)

    #   arg2: 9 -- diameter of neighborhood
    #   arg3: how much to focus on color difference
    #   arg4: how much to focus on space difference
    bilateral_denoised_img = cv2.bilateralFilter(noisy_image, 9, 75, 75)
    bilateral_denoised_img_rgb = cv2.cvtColor(bilateral_denoised_img, cv2.COLOR_BGR2RGB)

    plt.figure(figsize=(15, 10))
    #   args 1&2: specifies a 2 by 2 image
    plt.subplot(2, 2, 1)
    plt.title("Noisy Image")
    plt.imshow(noisy_image_rgb)
    plt.axis("off")

    plt.subplot(2, 2, 3)
    plt.title("Gaussian Denoised Image")
    plt.imshow(gaussian_denoised_img_rgb)
    plt.axis("off")
    
    plt.subplot(2, 2, 2)
    plt.title("Median Blur Image")
    plt.imshow(median_denoised_img_rgb)
    plt.axis("off")

    plt.subplot(2, 2, 4)
    plt.title("Bilateral Filtered Image")
    plt.imshow(bilateral_denoised_img_rgb)
    plt.axis("off")

    plt.show()



def main():
    denoise_image("source/noisy1.png")
    denoise_image("source/noisy2.png")
    denoise_image("source/noisy3.png")

if __name__ == "__main__":
    main()
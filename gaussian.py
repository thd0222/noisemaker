import numpy as np
import cv2


def generate_gaussian_noise(image, sigma):
    normal = np.random.normal(0, sigma, image.shape)
    return image + normal

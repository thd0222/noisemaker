import numpy as np
import cv2


def generate_gaussian_noise(image, var):
    normal = np.random.normal(0, var, image.shape)
    return image + normal

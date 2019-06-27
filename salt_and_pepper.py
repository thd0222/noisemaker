import numpy as np
import cv2


def generate_salt_and_pepper_noise(image, p):
    height, width = image.shape[0:2]
    n = int(width * height * p)
    x = np.random.choice(width, n)
    y = np.random.choice(height, n)
    value = np.random.choice([0, 255], n)

    result = image.copy()

    for x_, y_, v in zip(x, y, value):
        for c in range(image.shape[2]):
            result[y_][x_][c] = v

    return result

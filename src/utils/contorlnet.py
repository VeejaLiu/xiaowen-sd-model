import cv2
import numpy as np
from PIL import Image


def get_canny_image(image):
    np_image = np.array(image)

    # get canny image
    np_image = cv2.Canny(np_image, 100, 200)
    np_image = np_image[:, :, None]
    np_image = np.concatenate([np_image, np_image, np_image], axis=2)
    canny_image = Image.fromarray(np_image)

    return canny_image

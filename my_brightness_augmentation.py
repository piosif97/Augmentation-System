from augmentation import *
import time
import numpy as np


class MyBrightnessAugmentation(Augmentation):
    def __init__(self, list_of_parameters):
        Augmentation.__init__(self, list_of_parameters)
        print(self._list_of_parameters)

    def augment_image(self, original_image):
        dimensions = original_image.shape
        bias = int(self._list_of_parameters[0])
        augmented_image = np.zeros(dimensions, original_image.dtype)
        for j in range(dimensions[0]):
            for i in range(dimensions[1]):
                for color_channel in range(dimensions[2]):
                    augmented_image[j, i, color_channel] = np.clip(original_image[j, i, color_channel] + bias, 0, 255)
        return augmented_image

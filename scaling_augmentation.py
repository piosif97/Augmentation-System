from augmentation import *
import cv2
import numpy as np


class ScalingAugmentation(Augmentation):
    def __init__(self, list_of_parameters):
        Augmentation.__init__(self, list_of_parameters)
        print(self._list_of_parameters)

    def augment_image(self, original_image):
        height, width = original_image.shape[:2]
        ox_resize = int(self._list_of_parameters[0])
        oy_resize = int(self._list_of_parameters[1])
        new_width = int(width * ox_resize / 100)
        new_height = int(height * oy_resize / 100)
        new_size = (new_width, new_height)
        augmented_image = cv2.resize(original_image, new_size, interpolation=cv2.INTER_CUBIC)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(augmented_image, 'Scaling', (10, 450), font, 3, (199, 36, 177), 5, cv2.LINE_AA)
        return augmented_image

from augmentation import *
import cv2
import numpy as np


class FlippingAugmentation(Augmentation):
    def __init__(self, list_of_parameters):
        Augmentation.__init__(self, list_of_parameters)
        print(self._list_of_parameters)

    def augment_image(self, original_image):
        if self._list_of_parameters[0] == "VerticalFlip":
            augmented_image = cv2.flip(original_image, 0)
        else:
            if self._list_of_parameters[0] == "HorizontalFlip":
                augmented_image = cv2.flip(original_image, 1)
            else:
                augmented_image = cv2.flip(original_image, -1)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(augmented_image, 'Flipping', (10, 450), font, 3, (199, 36, 177), 5, cv2.LINE_AA)
        return augmented_image

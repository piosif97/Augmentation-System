from augmentation import *
import cv2
import numpy as np


class ContrastAugmentation(Augmentation):
    def __init__(self, list_of_parameters):
        Augmentation.__init__(self, list_of_parameters)
        print(self._list_of_parameters)

    def augment_image(self, original_image):
        dimensions = original_image.shape
        augmented_image = np.zeros(dimensions, original_image.dtype)
        gain = float(self._list_of_parameters[0])
        augmented_image = cv2.addWeighted(original_image, gain, augmented_image, 0, 0)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(augmented_image, 'Contrast', (10, 450), font, 3, (199, 36, 177), 5, cv2.LINE_AA)
        return augmented_image

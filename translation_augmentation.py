from augmentation import *
import cv2
import numpy as np


class TranslationAugmentation(Augmentation):
    def __init__(self, list_of_parameters):
        Augmentation.__init__(self, list_of_parameters)
        print(self._list_of_parameters)

    def augment_image(self, original_image):
        # the parameters are equivalent to the number of pixels the image should be moved by in a certain direction
        height, width = original_image.shape[:2]
        ox_translation = int(self._list_of_parameters[0])
        oy_translation = int(self._list_of_parameters[1])
        M = np.float32([[1, 0, ox_translation], [0, 1, oy_translation]])
        augmented_image = cv2.warpAffine(original_image, M, (width, height))
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(augmented_image, 'Translation', (10, 450), font, 3, (199, 36, 177), 5, cv2.LINE_AA)
        return augmented_image

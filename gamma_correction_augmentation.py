from augmentation import *
import cv2
import numpy as np


class GammaCorrectionAugmentation(Augmentation):
    def __init__(self, list_of_parameters):
        Augmentation.__init__(self, list_of_parameters)
        print(self._list_of_parameters)

    def augment_image(self, original_image):
        # build a lookup table mapping the pixel values [0, 255] to their adjusted gamma values
        # LUT works on the standard 8-bit format
        gamma = float(self._list_of_parameters[0])
        inverse_of_gamma = 1.0 / gamma
        # the intensity of the pixels must be scaled from the range [0, 255] to [0, 1] and afterwards scaled back
        lookup_table = np.array([((i / 255) ** inverse_of_gamma) * 255 for i in np.arange(0, 256)])
        augmented_image = cv2.LUT(original_image, lookup_table)
        # font = cv2.FONT_HERSHEY_SIMPLEX
        # cv2.putText(augmented_image, 'Gamma Correction', (10, 450), font, 3, (199, 36, 177), 5, cv2.LINE_AA)
        return augmented_image

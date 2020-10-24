from augmentation import *
import cv2
import numpy as np


class ConvolutionFilterAugmentation(Augmentation):
    def __init__(self, list_of_parameters):
        Augmentation.__init__(self, list_of_parameters)
        print(self._list_of_parameters)

    def augment_image(self, original_image):
        size = int(self._list_of_parameters[0])
        kernal = np.zeros((size, size), dtype=float)
        kernal = np.fromstring(self.construct_string_from_parameters(), float, sep=" ").reshape(kernal.shape)
        augmented_image = cv2.filter2D(original_image, -1, kernal)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(augmented_image, 'Convolution', (10, 450), font, 3, (199, 36, 177), 5, cv2.LINE_AA)
        return augmented_image

    def construct_string_from_parameters(self):
        s = ""
        for parameter in self._list_of_parameters[1:]:
            s = s + parameter + " "
        s = s[: len(s) - 1]
        return s
    
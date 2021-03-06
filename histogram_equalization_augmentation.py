from augmentation import *
import cv2
import numpy as np


class HistogramEqualizationAugmentation(Augmentation):
    def __init__(self, list_of_parameters):
        Augmentation.__init__(self, list_of_parameters)
        print(self._list_of_parameters)

    def augment_image(self, original_image):
        dimensions = original_image.shape
        augmented_image = np.zeros(dimensions, original_image.dtype)
        np.copyto(augmented_image, original_image)
        hls = cv2.cvtColor(augmented_image, cv2.COLOR_BGR2HLS)
        channels = cv2.split(hls)
        cv2.equalizeHist(channels[1], channels[1])
        cv2.merge(channels, hls)
        cv2.cvtColor(hls, cv2.COLOR_HLS2BGR, augmented_image)
        # font = cv2.FONT_HERSHEY_SIMPLEX
        # cv2.putText(augmented_image, 'Histogram Equalization', (10, 450), font, 3, (199, 36, 177), 5, cv2.LINE_AA)
        return augmented_image


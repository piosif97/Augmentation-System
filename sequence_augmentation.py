from augmentation import *
import cv2
import numpy as np
import glob
from blank_augmentation import *
from rotation_augmentation import *
from brightness_augmentation import *
from contrast_augmentation import *
from gamma_correction_augmentation import *
from histogram_equalization_augmentation import *
from convolution_filter_augmentation import *
from translation_augmentation import *
from flipping_augmentation import *
from scaling_augmentation import *
from sequence_augmentation import *
from my_brightness_augmentation import  *

class SequenceAugmentation(Augmentation):
    def __init__(self, list_of_parameters):
        Augmentation.__init__(self, list_of_parameters)
        print(self._list_of_parameters)
        self.__list_of_augmentations = self.construct_list_of_augmentations()

    def construct_list_of_augmentations(self):
        augmentations = []
        for parameter in self._list_of_parameters:
            augmentation_parameters = parameter.split(sep=" ")
            augmentation_class = globals()[augmentation_parameters[0] + "Augmentation"]
            augmentation = augmentation_class(augmentation_parameters[1:])
            augmentations.append(augmentation)
        return augmentations

    def augment_image(self, original_image):
        for augmentation in self.__list_of_augmentations:
            original_image = augmentation.augment_image(original_image)
        return original_image

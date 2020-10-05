from augmentation import *


class BlankAugmentation(Augmentation):
    def __init__(self, list_of_parameters):
        Augmentation.__init__(self, list_of_parameters)
        print(self._list_of_parameters)

    def augment_image(self, original_image):
        return original_image

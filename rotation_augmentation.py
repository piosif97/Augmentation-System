from augmentation import *
import cv2

class RotationAugmentation(Augmentation):
    def __init__(self, list_of_parameters):
        Augmentation.__init__(self, list_of_parameters)
        print(self._list_of_parameters)

    def augment_image(self, original_image):
        angle = float(self._list_of_parameters[0])
        height, width = original_image.shape[:2]
        M = cv2.getRotationMatrix2D((width/2, height/2), angle, 1)
        augmented_image = cv2.warpAffine(original_image, M, (width, height))
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(augmented_image, 'Rotation', (10, 450), font, 3, (199, 36, 177), 5, cv2.LINE_AA)
        return augmented_image

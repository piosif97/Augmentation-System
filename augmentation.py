import abc


class Augmentation(abc.ABC):
    def __init__(self, list_of_parameters):
        self._list_of_parameters = list_of_parameters

    @abc.abstractmethod
    def augment_image(self, original_image):
        pass

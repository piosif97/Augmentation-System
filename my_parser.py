class MyParser(object):

    def __init__(self, config_file):
        self.__lines = config_file.readlines()

    def get_configuration_file_validity(self):
        if len(self.__lines) > 0:
            for line in self.__lines:
                if not self.is_line_valid(line.strip()):
                    return self.__lines.index(line) + 1
        else:
            return -2
        return -1

    def are_brightness_parameters_valid(self, parameters):
        if len(parameters) != 1:
            return False
        if not self.is_integer(parameters[0]):
            return False
        return True

    def are_contrast_parameters_valid(self, parameters):
        if len(parameters) != 1:
            return False
        if not self.is_positive_float(parameters[0]):
            return False
        return True

    def are_gamma_correction_parameters_valid(self, parameters):
        if len(parameters) != 1:
            return False
        if not self.is_positive_float(parameters[0]):
            return False
        return True

    def are_histogram_equalization_paramaters_valid(self, parameters):
        if len(parameters) == 0:
            return True
        return False

    def are_convolution_filter_parameters_valid(self, parameters):
        if not self.is_positive_uneven_integer(parameters[0]):
            return False
        size = int(parameters[0]) * int(parameters[0])
        if (len(parameters) - 1) != size:
            return False
        for parameter in parameters[1:]:
            if not self.is_float(parameter):
                return False
        return True

    def are_translation_parameters_valid(self, parameters):
        if not len(parameters) == 2:
            return False
        if (not self.is_positive_integer(parameters[0])) and (not self.is_positive_integer(parameters[1])):
            return False
        return True

    def are_flipping_parameters_valid(self, parameters):
        if not len(parameters) == 1:
            return False
        if (parameters[0] == "VerticalFlip") or (parameters[0] == "HorizontalFlip") or \
                (parameters[0] == "BothDirectionsFlip"):
            return True
        return False

    def are_rotation_parameters_valid(self, parameters):
        if not len(parameters) == 1:
            return False
        if self.is_float(parameters[0]):
            return True
        return False

    def are_scaling_parameters_valid(self, parameters):
        if not len(parameters) == 2:
            return False
        if (self.is_positive_integer(parameters[0])) and (self.is_positive_integer(parameters[1])):
            return True
        return False

    def invalid_augmentation(self, parameters):
        return False

    def is_augmentation_valid(self, augmentation_name, augmentation_parameters):
        switcher = {
            "Brightness": self.are_brightness_parameters_valid,
            "Contrast": self.are_contrast_parameters_valid,
            "GammaCorrection": self.are_gamma_correction_parameters_valid,
            "HistogramEqualization": self.are_histogram_equalization_paramaters_valid,
            "ConvolutionFilter": self.are_convolution_filter_parameters_valid,
            "Translation": self.are_translation_parameters_valid,
            "Flipping": self.are_flipping_parameters_valid,
            "Rotation": self.are_rotation_parameters_valid,
            "Scaling": self.are_scaling_parameters_valid
        }
        function = switcher.get(augmentation_name, self.invalid_augmentation)
        return function(augmentation_parameters)

    def is_line_valid(self, line):
        parameters = line.split(sep=" ")
        return self.is_augmentation_valid(parameters[0], parameters[1:])

    def is_float(self, x):
        try:
            float(x)
            return True
        except ValueError:
            return False

    def is_integer(self, x):
        try:
            float(x)
        except ValueError:
            return False
        else:
            return float(x).is_integer()

    def is_positive_integer(self, x):
        try:
            float(x)
        except ValueError:
            return False
        else:
            if float(x).is_integer():
                return float(x) >= 0
            else:
                return False

    def is_positive_uneven_integer(self, x):
        if not self.is_positive_integer(x):
            return False
        else:
           return int(x) % 2 == 1

    def is_positive_float(self, x):
        try:
            float(x)
            if float(x) >= 0:
                return True
            else:
                return False
        except ValueError:
            return False

    def get_number_of_lines_in_config_file(self):
        return len(self.__lines)

    def get_list_of_attributes_in_line_of_config_file_at_position(self, position):
        return self.__lines[position].replace("\n", "").split(sep=" ")

    def get_config_file_content(self):
        s = ""
        for line in self.__lines:
            s += line
        return s

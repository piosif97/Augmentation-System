class MyParser(object):
    ACCEPTED_AUGMENTATIONS = ["Blank", "Rotation", "Tint"]
    ACCEPTED_COLORS = ["red", "blue", "green", "yellow", "pink", "purple"]

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

    def is_line_valid(self, line):
        parameters = line.split(sep=" ")
        if not (parameters[0] in self.ACCEPTED_AUGMENTATIONS):
            return False
        if len(parameters) > 1 and not (parameters[1] in self.ACCEPTED_COLORS) and not (parameters[1].isnumeric()):
            return False
        if len(parameters) > 2 and not (parameters[2].isnumeric()):
            return False
        return True

    def get_number_of_lines_in_config_file(self):
        return len(self.__lines)

    def get_list_of_attributes_in_line_of_config_file_at_position(self, position):
        return self.__lines[position].replace("\n", "").split(sep=" ")

    def get_config_file_content(self):
        s = ""
        for line in self.__lines:
            s += line
        return s

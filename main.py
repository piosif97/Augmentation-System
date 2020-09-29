from gui import *
from on_input_directory_ready_callback import *
from my_parser import *
from blank_augmentation import *
from rotation_augmentation import *
from tint_augmentation import *
import sys
import os
import shutil
import cv2

AUGMENTATION_PACKAGE_NAME = "augmentations"
CONFIG_FILE_PATH = "config.txt"

class Main(OnInputDirectoryReadyCallback):
    def on_input_directory_ready_callback(self, input_directory):
        self.create_output_directory(input_directory + "_aug")
        count = 1
        list_of_input_files_names = os.listdir(input_directory)
        dictionary_of_original_images = {}
        dictionary_of_augmentations = {}
        dictionary_of_new_images = {}
        for file_name in list_of_input_files_names:
            dictionary_of_original_images[file_name] = cv2.imread(input_directory + "/" + file_name)
        for i in range(self.__parser.get_number_of_lines_in_config_file()):
            list_of_attributes = self.__parser.get_list_of_attributes_in_line_of_config_file_at_position(i)
            augmentation_class = globals()[list_of_attributes[0] + "Augmentation"]
            augmentation = augmentation_class(list_of_attributes[1:])
            dictionary_of_augmentations[list_of_attributes[0] + str(i)] = augmentation
        for augmentation_id in dictionary_of_augmentations:
            for original_image_name in dictionary_of_original_images:
                new_image_name = original_image_name.replace(".jpg", "") + "_" \
                                 + augmentation_id[0:len(augmentation_id) - 1] + "_" + str(count) + ".jpg"
                count += 1
                dictionary_of_new_images[new_image_name] = dictionary_of_augmentations[augmentation_id].\
                    augment_image(dictionary_of_original_images[original_image_name])
        self.write_new_images_to_output_directory(dictionary_of_new_images)
        self.__gui.display_images(self.__output_directory_path)

    def write_new_images_to_output_directory(self, dictionary_of_new_images):
        for new_image_name in dictionary_of_new_images:
            cv2.imwrite(self.__output_directory_path + "/" + new_image_name, dictionary_of_new_images[new_image_name])

    def create_output_directory(self, directory_name):
        self.__output_directory_path = directory_name
        if os.path.exists(directory_name):
            shutil.rmtree(directory_name, True)
        os.mkdir(directory_name)

    def main(self):
        self.__parser = MyParser(open(CONFIG_FILE_PATH, "r"))
        result = self.__parser.get_configuration_file_validity()
        if result == -2:
            sys.exit("Configuration file is empty")
        if result != -1:
            sys.exit("Configuration file is not valid at line " + str(result))
        self.__gui = Gui(self, self.__parser.get_config_file_content())
        self.__gui.create_gui()


main = Main()
main.main()
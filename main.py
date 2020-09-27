import cv2
from gui import *
from on_input_directory_ready_callback import *
from my_parser import *
import sys

CONFIG_FILE = "config.txt"


class Main(OnInputDirectoryReadyCallback):
    def on_input_directory_ready_callback(self, input_directory):
        print(input_directory)

    def main(self):
        parser = MyParser(open(CONFIG_FILE, "r"))
        result = parser.get_configuration_file_validity()
        if result == -2:
            sys.exit("Configuration file is empty")
        if result != -1:
            sys.exit("Configuration file is not valid at line " + str(result))
        gui = Gui(self, parser.get_config_file_content())
        gui.create_gui()


main = Main()
main.main()
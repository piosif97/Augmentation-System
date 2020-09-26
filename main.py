import cv2
from gui import *
from on_input_directory_ready_callback import *


class Main(OnInputDirectoryReadyCallback):
    def on_input_directory_ready_callback(self, input_directory):
        print(input_directory)

    def main(self):
        gui = Gui("650x500", self)
        gui.create_gui()


main = Main()
main.main()
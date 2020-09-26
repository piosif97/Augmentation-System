from tkinter import *
from tkinter import filedialog


class Gui(object):
    def __init__(self, window_size, callback):
        self.__root = Tk()
        self.__root.title("Augmentation System")
        self.__root.geometry(window_size)
        self.__selected_directory = ""
        self.__callback = callback

    def on_click_select_directory(self):
        self.__selected_directory = filedialog.askdirectory(initialdir="c://Users//Patricia",
                                                            title="Select A Directory")
        selected_directory_name_label = Label(self.__root,
                                              text="The selected directory is: " + self.__selected_directory)
        selected_directory_name_label.pack(fill="none", expand=True)
        self.__callback.on_input_directory_ready_callback(self.__selected_directory)

    def create_gui(self):
        selected_directory_label = Label(self.__root, text="Press the button to select a directory containing images " +
                                                           "you wish to augment: ")
        selected_directory_label.pack(fill="none", expand=True)
        select_directory_button = Button(self.__root, text="Select directory", command=self.on_click_select_directory)
        select_directory_button.pack(fill="none", expand=True)
        self.__root.mainloop()

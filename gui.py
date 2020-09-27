from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from PIL import ImageTk, Image
import glob


class Gui(object):
    def __init__(self, callback, config_file_content):
        self.__root = Tk()
        self.__root.title("Augmentation System")
        self.__root.state("zoomed")
        self.__callback = callback
        self.__config_file_content = config_file_content
        self.__scrollable_frame = self.create_scrollable_window()
        self.__current_row = 0

    def create_scrollable_window(self):
        main_frame = Frame(self.__root)
        main_frame.pack(fill=BOTH, expand=1)
        canvas = Canvas(main_frame)
        canvas.pack(side=LEFT, fill=BOTH, expand=1)
        scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=canvas.yview)
        scrollbar.pack(side=RIGHT, fill=Y)
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        scrollable_frame = Frame(canvas)
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        for thing in range(1000):
            Label(scrollable_frame, text="").grid(row=thing, column=0)
        return scrollable_frame

    def create_gui(self):
        config_file_content_label = Label(self.__scrollable_frame, text="Config file content:\n" +
                                                                        self.__config_file_content)
        config_file_content_label.grid(row=self.__current_row, column=0, columnspan=3)
        self.increase_current_row()
        selected_directory_label = Label(self.__scrollable_frame,
                                         text="Press the button to select a directory containing images " +
                                              "you wish to augment: ")
        selected_directory_label.grid(row=self.__current_row, column=0, columnspan=3)
        self.increase_current_row()
        select_directory_button = Button(self.__scrollable_frame, text="Select directory",
                                         command=self.on_click_select_directory)
        select_directory_button.grid(row=self.__current_row, column=0, columnspan=3)
        self.increase_current_row()
        self.__root.mainloop()

    def increase_current_row(self):
        self.__current_row += 1

    def on_click_select_directory(self):
        selected_directory = filedialog.askdirectory(initialdir="c://Users//Patricia", title="Select A Directory")
        selected_directory_name_label = Label(self.__scrollable_frame,
                                              text="The input directory is: " + selected_directory)
        selected_directory_name_label.grid(row=self.__current_row, column=0, columnspan=3)
        self.display_images(selected_directory)
        self.__callback.on_input_directory_ready_callback(selected_directory)

    def display_images(self, directory):
        self.increase_current_row()
        current_column = 0
        list_of_image_paths = glob.glob(directory + "/*.jpg")
        images = []
        labels = []
        i = 0
        for path in list_of_image_paths:
            image = Image.open(path)
            image = image.resize((320, 240), Image.ANTIALIAS)
            image = ImageTk.PhotoImage(image)
            images.append(image)
            labels.append(Label(self.__scrollable_frame, image=images[i]))
            labels[i].image = images[i]
            if i % 3 == 0 and i > 0:
                self.increase_current_row()
                current_column = 0
            labels[i].grid(row=self.__current_row, column=current_column)
            current_column += 1
            i += 1

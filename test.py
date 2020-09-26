import cv2
from tkinter import *
from tkinter import filedialog

root = Tk()
root.geometry("600x500")


def create_gui():
    root.title("Augmentation System")
    selected_directory_label = Label(root, text="Press the button to select a directory containing images " +
                                                "you wish to augment: ")
    selected_directory_label.grid(row=0, column=0)
    select_directory_button = Button(root, text="Select directory", command=on_click_select_directory)
    select_directory_button.grid(row=0, column=1)
    root.mainloop()


def on_click_select_directory():
    selected_directory = filedialog.askdirectory(initialdir="c://Users//Patricia", title="Select A Directory")
    selected_directory_name_label = Label(root, text="The selected directory is: " + selected_directory)
    selected_directory_name_label.grid(row=1, column=0)


create_gui()





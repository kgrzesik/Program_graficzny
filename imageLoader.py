from PIL import ImageTk
from picture import Picture
from tkinter import filedialog
from tkinter import *
class ImageLoader():
    def open(self):
        path = filedialog.askopenfilenames()
        return [Picture(img_path) for img_path in path]


from tkinter import *
from PIL import ImageTk
from PIL import ImageFilter 
import PIL.ImageTk as ptk
from abc import ABC, abstractclassmethod
import copy

import copy

class Plugin(ABC):
    @abstractclassmethod
    def filter(self):
        pass

class Blur(Plugin):
    def filter(self,pic):
        new_pic = copy.copy(pic)
        new_pic.image=new_pic.image.filter(ImageFilter.GaussianBlur(radius = 5))
        new_pic.new_size=new_pic.image.resize((new_pic.w,new_pic.h))
        new_pic.img=ptk.PhotoImage(new_pic.new_size)
        return new_pic

class Mono(Plugin):
    def filter(self,pic):
        new_pic = copy.copy(pic)
        new_pic.image=new_pic.image.convert('L')
        new_pic.new_size=new_pic.image.resize((new_pic.w,new_pic.h))
        new_pic.img=ptk.PhotoImage(new_pic.new_size)
        return new_pic

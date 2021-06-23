import PIL as p
import PIL.ImageTk as ptk
class Picture():
    def __init__(self,path):
        self.image = p.Image.open(path)
        self.width, self.height = self.image.size
        self.w=int(self.width/2)
        self.h=int(self.height/2)
        self.new_size=self.image.resize((self.w,self.h))
        self.img=ptk.PhotoImage(self.new_size)
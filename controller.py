from os import path
from tkinter.constants import FALSE, TRUE
from imageLoader import ImageLoader
from plugin import Mono
from plugin import Blur
from tkinter.filedialog import asksaveasfile
from photoMenager import PhotoManager
from tkinter import filedialog

class Controller():
    def __init__(self):
        self.photos=[]
        self.currentPhotoManager=0
        self.il=ImageLoader()

    def goBack(self):
       self.photos[self.currentPhotoManager].setPreviousActive()

    def goNext(self):
        self.photos[self.currentPhotoManager].setNextActive()

    def addPictute(self):
        self.photos+=[PhotoManager(photo) for photo in self.il.open()]

    def getNumberOfPhotos(self):
        return len(self.photos)

    def removeCurrentPhoto(self):
        if self.photos:
            if self.currentPhotoManager==self.getNumberOfPhotos()-1 and self.currentPhotoManager!=0:
                del self.photos[self.currentPhotoManager]
                self.currentPhotoManager-=1
            else:
                del self.photos[self.currentPhotoManager]             
        
    def getCurrentPicture(self):
        if self.photos:
            return self.photos[self.currentPhotoManager].getImg()
        return None
    
    def updateNext(self):
        if self.currentPhotoManager<self.getNumberOfPhotos()-1:
            self.currentPhotoManager += 1
    
    def updatePreview(self):
        if self.currentPhotoManager>0:
            self.currentPhotoManager -= 1
    
    def addPlugin(self,number):
        func = {
            "Mono": Mono(),
            "Blur": Blur(),
        }.get(number, lambda x: x)
        if self.photos is not None:
            new_photo = func.filter(self.photos[self.currentPhotoManager].getCurrentPhoto())
            self.photos[self.currentPhotoManager].addList(number)
            self.photos[self.currentPhotoManager].addHistory(new_photo)
        
    def getShowList(self):
        return self.photos[self.currentPhotoManager].getList()
        

    def saveFile(self):
        files = [('All Files', "*.*"), 
             ('JPG', "*.jpg"),
             ('PNG', "*.png"),
             ('RAW', "*.NEF"),
             ('WebP', "*.webp"),
             ('JPeG', "*.jpeg"),
             ('GIF', "*.gif")]
        file = asksaveasfile(filetypes = files, defaultextension = files)
        self.photos[self.currentPhotoManager].getImage().save(file.name)

    def saveList(self):
        files = [('TXT', "*.txt")]
        file = asksaveasfile(filetypes = files, defaultextension = files)
        print(file.name)
        with open(file.name,'w+',encoding='utf-8') as f:
            for x in range(len(self.photos[self.currentPhotoManager].getList())):
                f.write('%s\n' %self.photos[self.currentPhotoManager].getList()[x])
    
            
    
    def openList(self):
        path = filedialog.askopenfilename()
        print(path)
        with open(path) as ff:
            contents = ff.readlines()
            print(contents)
        for x in contents:
            content=x.strip()
            self.addPlugin(content)
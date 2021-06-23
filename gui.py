from tkinter import *
import tkinter as tkr
from controller import Controller


class Gui():
    def __init__(self, title, geometry):
        self.root=Tk()
        self.root.title(title)
        self.root.geometry(geometry)
        self.addPhotoButton()
        self.createMenu()
        self.control = Controller()
        self.toolBar()
        self.label = tkr.Label(self.root)
        self.labelList = tkr.Label(self.root)
        self.root.mainloop()
        
    def addPhotoButton(self):
        self.adder=Button(self.root, text="Dodaj zdjęcie/zdjecia", command=self.showPicture)
        self.adder.grid(column=1,row=1,columnspan=7)

    def createMenu(self):
        menubar = Menu(self.root)
        self.barFile(menubar)
        self.barEdition(menubar)
        self.barHelp(menubar)
        self.root.config(menu=menubar)

    def barFile(self,menubar):
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Open", command=self.showPicture)
        filemenu.add_command(label="Save", command=self.save)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.root.quit)
        menubar.add_cascade(label="Plik", menu=filemenu)

    def barEdition(self,menubar):
        editmenu = Menu(menubar, tearoff=0)
        editmenu.add_command(label="Undo", command=self.doUndo)
        editmenu.add_separator()
        menubar.add_cascade(label="Edycja", menu=editmenu)

    def barHelp(self,menubar):
        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_command(label="Help Index", command=self.Jakaś_funkcja)
        helpmenu.add_command(label="About...", command=self.Jakaś_funkcja)
        menubar.add_cascade(label="Pomoc", menu=helpmenu)

    def showPicture(self):
        self.control.addPictute()
        self.updatePicture()
        self.adder.grid_forget()

    def updatePicture(self):
        self.label.grid_forget()
        photo = self.control.getCurrentPicture()
        if photo is not None:
            list=self.control.getShowList()
            self.label = tkr.Label(self.root,image=photo)
            self.label.grid(column=1,row=2,columnspan=7,rowspan=100)
            if list is not None:
                self.showList(list)
        if photo is None:
            self.addPhotoButton()

    def hidePicture(self):
        self.label.grid_forget()

    def hideList(self):
        self.labelList.grid_forget()

    def addMono(self):
        self.control.addPlugin("Mono")
        self.updatePicture()

    def addBlur(self):
        self.control.addPlugin("Blur")
        self.updatePicture()

    def preview(self):
        self.hidePicture()
        self.control.updatePreview()
        self.updatePicture()

    def next(self):
        self.hidePicture()
        self.control.updateNext()
        self.updatePicture()

    def save(self):
        self.control.saveFile()

    def remove(self):
        self.hideList()
        self.control.removeCurrentPhoto()
        self.updatePicture()

    def doUndo(self):
        self.control.goBack()
        self.updatePicture()
    
    def doRedo(self):
        self.control.goNext()
        self.updatePicture()

    def showList(self, list):
        self.hideList()
        self.labelList=Label(self.root, text=list)
        self.labelList.grid(column=0,row=1, columnspan=1000)

    def saveL(self):
        self.control.saveList()
        self.updatePicture()
    
    def openL(self):
        self.control.openList()
        self.updatePicture()

    def toolBar(self):
        mono=Button(self.root, text="Mono", command=self.addMono)
        mono.grid(column=0,row=0)
        blur=Button(self.root, text="Blur", command=self.addBlur)
        blur.grid(column=1,row=0)
        mono=Button(self.root, text="<--", command=self.preview)
        mono.grid(column=4,row=0)
        blur=Button(self.root, text="-->", command=self.next)
        blur.grid(column=5,row=0)
        blur=Button(self.root, text="X", command=self.remove)
        blur.grid(column=8,row=0)
        blur=Button(self.root, text="Undo", command=self.doUndo)
        blur.grid(column=2,row=0)
        blur=Button(self.root, text="Redo", command=self.doRedo)
        blur.grid(column=3,row=0)
        blur=Button(self.root, text="Pobierz liste filtrów", command=self.saveL)
        blur.grid(column=6,row=0)
        blur=Button(self.root, text="Otwórz liste filtrów", command=self.openL)
        blur.grid(column=7,row=0)


    def Jakaś_funkcja(self):
        filewin = Toplevel(self.root)
        button = Button(filewin, text="Funkcja do podstawienia")
        button.pack()
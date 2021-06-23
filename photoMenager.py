class PhotoManager:
    def __init__(self,pic):
        self.current=0
        self.history=[pic]
        self.list=[]

    def getHistory(self):
        return self.history

    def addHistory(self,pic):
        self.history[self.current+1:len(self.history)]=[]
        self.list[self.current+1:len(self.history)]=[]
        self.history.append(pic)
        self.current+=1

    def getImg(self):
        return self.history[self.current].img

    def getImage(self):
        return self.history[self.current].image

    def getCurrentPhoto(self):
        return self.history[self.current]

    def setPreviousActive(self):
        if self.current != 0:
            self.current -= 1

    def setNextActive(self):
        if self.current != len(self.history)-1:
            self.current += 1

    def addList(self,num):
        func = {
            "Mono": "Mono",
            "Blur": "Blur",
        }.get(num, "Undefined")
        self.list[self.current:len(self.history)]=[]
        self.list.append(func)

    def getList(self):
        print(self.list[:self.current])
        return self.list[:self.current]


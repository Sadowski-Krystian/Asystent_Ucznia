from os import stat
import tkinter as tk
from tkinter import *

class AsystentUcznia(tk.Tk):

    def __init__(self):
        super().__init__()
        # self = Tk()
        self.title("Asystent ucznia")
        self.win_hei = 70
        self.win_wid = 200
        self.scr_hei = self.winfo_screenheight()
        self.scr_wid = self.winfo_screenwidth()
        print(str(self.scr_hei))
        print(str(self.scr_wid))
        self.place_x = self.scr_wid - self.win_wid
        self.place_y = 20
        self.offset = "+"+str(self.place_x)+"+"+str(self.place_y)
        self.geometry(str(self.win_wid)+"x"+str(self.win_hei)+self.offset)
        self.isFullScreen = False
        self.splashScreen()
   

    def quitApp(self):
        print("Zamykam program")
        self.quit()

    def saveData(self, list1, name1, pass1):
        plik = "user.txt"
        data = list1+";"+name1
        out = False
        with open(plik, 'w') as writer:
            writer.write(data)
            out = True
        return out

    def goNext(self):
        print("Naciśnięto przycisk")
        list1 = self.lsb.curselection()
        if(list1):
            list1 = self.lsb.get(self.lsb.curselection())
        else:
            list1 = None
        name1 = self.ent2.get()
        pass1 = self.ent3.get()

        if( list1 == None or name1=='' or pass1 == ''):
            print("puste")
            return

        state = self.saveData(list1, name1, pass1)
        if(state == False):
            print("nie zapisano")
            return

        self.box.pack_forget()

        self.fullScreen()
        self.renderUi()
    
    def notify(self):
        print("some notifi")

    def getTaskList(self):
        print("Get Task list")

    def fullScreen(self):
        self.isFullScreen
        if(self.isFullScreen):
            self.isFullScreen = False
            self.attributes("-fullscreen", False) #tylko dla linuxas
        else:
            self.isFullScreen = True
            self.attributes("-fullscreen", True) #tylko dla linuxa
            

    def buildSelect(self, selBox):
        box1 = Frame(selBox, height=100, width=10)
        lstItemsArr = ["1a", "2b", "3c", "4d", "5e", "6f", "7g", "8h", "9i", ]
        lstItems = StringVar(value=lstItemsArr)
        scb = Scrollbar(box1, orient=VERTICAL)
        self.lsb = Listbox(box1, listvariable=lstItems, selectmode=BROWSE, height=4, width=8, yscrollcommand=scb.set)
        self.lsb.pack(side=LEFT)
        scb.pack(side=LEFT)
        scb.config(command=self.lsb.yview)
        return box1

    def splashScreen(self):
        self.fullScreen()
        self.box = Frame(self)
        lbl1 = Label(self.box, text="Wybierz klasę")
        lbl2 = Label(self.box, text="Podaj nazwisko")
        lbl3 = Label(self.box, text="Podaj hasło")
        sel1 = Frame(self.box)
        self.buildSelect(sel1).pack()
        self.ent2 = Entry(self.box)
        self.ent3 = Entry(self.box)
        btnSet = Button(self.box, text="Dalej", command=self.goNext)
        lbl1.grid(row=1, column=1)
        lbl2.grid(row=1, column=2)
        lbl3.grid(row=1, column=3)
        btnSet.grid(row=1, column=4)
        self.ent2.grid(row=2, column=2)
        self.ent3.grid(row=2, column=3)
        sel1.grid(row=2, column=1)
        self.box.pack(fill=BOTH)







    def renderUi(self):


        grd = Frame(self)

        btnTaskOk = Button(grd, text="OK", command=self.notify)
        btnTaskLst = Button(grd, text="LS", command=self.getTaskList)
        btnFullScr = Button(grd, text="FS", command=self.fullScreen)
        btnAppQit = Button(grd, text="Q", command=self.quitApp)

        btnTaskOk.grid(row="1", column="1")
        btnTaskLst.grid(row="1", column="2")
        btnFullScr.grid(row="1", column="3")
        btnAppQit.grid(row="1", column="4")
        grd.pack(side=LEFT)

if(__name__=="__main__"):
    app = AsystentUcznia()
    app.mainloop()
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
        self.renderUi()
   

    def quitApp(self):
        print("Zamykam program")
        self.quit()

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
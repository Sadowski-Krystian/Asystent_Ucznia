from tkinter import *

win = Tk()
win.title("Asystent ucznia")
win_hei = 70
win_wid = 200
scr_hei = win.winfo_screenheight()
scr_wid = win.winfo_screenwidth()
print(str(scr_hei))
print(str(scr_wid))
place_x = scr_wid - win_wid
place_y = 20
offset = "+"+str(place_x)+"+"+str(place_y)

win.geometry(str(win_wid)+"x"+str(win_hei)+offset)

isFullScreen = False

def quitApp():
    print("Zamykam program")
    win.quit()

def notify():
    print("some notifi")

def getTaskList():
    print("Get Task list")

def fullScreen():
    global isFullScreen
    if(isFullScreen):
        isFullScreen = False
        win.attributes("-fullscreen", False) #tylko dla linuxas
    else:
        isFullScreen = True
        win.attributes("-fullscreen", True) #tylko dla linuxa
        
    

grd = Frame(win)

btnTaskOk = Button(grd, text="OK", command=notify)
btnTaskLst = Button(grd, text="LS", command=getTaskList)
btnFullScr = Button(grd, text="FS", command=fullScreen)
btnAppQit = Button(grd, text="Q", command=quitApp)

btnTaskOk.grid(row="1", column="1")
btnTaskLst.grid(row="1", column="2")
btnFullScr.grid(row="1", column="3")
btnAppQit.grid(row="1", column="4")
grd.pack(side=LEFT)
btnSet = Button(win, text="Dalej")
btnSet.pack(side=LEFT)

mainloop()
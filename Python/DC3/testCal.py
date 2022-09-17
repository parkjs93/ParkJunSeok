from statistics import mean
from tkinter import *
import tkinter.ttk
from tkinter.ttk import LabelFrame

window = tkinter.Tk()

window.title("UI test")
window.geometry("300x300+100+100")
window.resizable(False,False)

def close():
    a="https://jiralive.nexon.com/browse/MSKR-51710"
    indexMAKR=a.index("M")
    print(indexMAKR)
    b=a[indexMAKR:indexMAKR+11]
    print(b)


    window.quit()
    window.destroy()

mainMenu=Menu(window)
window.config(menu=mainMenu)

fileMenu=Menu(mainMenu, tearoff=0)
mainMenu.add_cascade(label="일번", menu=fileMenu)
fileMenu.add_command(label="음")
fileMenu.add_separator()
fileMenu.add_command(label="exit", command=close)

window.mainloop()

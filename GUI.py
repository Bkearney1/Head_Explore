#uses archiveSearch and makes a little GUI
from tkinter import *
import webbrowser
import archiveSearcher

def run():

    #begin buttons
    root = Tk()
    root.title('HeadFinder')
    root.geometry("300x805")
    root.iconbitmap(r'C:\Users\Brett\PycharmProjects\grateexplore\favicon.ico')#I do not own the "steal your face" logo

    for i in range(1965,1996):
        x=str(i)
        x=Button(root,text=x,bg="NavajoWhite3",fg="black",command=lambda i=i :archiveSearcher.findYear(i)) #
        x.pack(side=TOP,fill=X)

    root.mainloop()

()





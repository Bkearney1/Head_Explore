#uses archiveSearch and makes a little GUI
from tkinter import *
from tkinter import messagebox
import archiveSearcher
import webScraper

def run():

    #begin GUI stuff
    root = Tk()
    root.title('HeadFinder')
    root.geometry("300x805")
    root.iconbitmap(r'favicon.ico')#adds steal your face as a favicon

    def command():
        Toplevel(root)


    button = Button(root, text="Favorites", command=command)
    button.pack( side = TOP, fill = X)

    for i in range(1965,1996):
        x=str(i)
        x=Button(root,text=x,bg="NavajoWhite3",fg="black",command=lambda i=i :archiveSearcher.findYear(i)) #
        x.pack(side=TOP,fill=X)

    def on_closing():
        if messagebox.askokcancel("Quit HeadFinder?", "Do you want to quit?"):
            root.destroy()
    root.protocol("WM_DELETE_WINDOW", on_closing)

    root.mainloop()

()





#uses archiveSearch and makes a little GUI
from tkinter import *
from tkinter import messagebox

from webScraper import  *
import webScraper

def searchTheArchive(year):
    webScraper.find_item(year)
    webScraper.findTitle(year)

    num_items = len(item_text)

    for x in range(0, num_items):
        print(item_name[x] + "  :  http://archive.org/details/" + item_text[x])
    ()

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
        x=Button(root,text=x,bg="NavajoWhite3",fg="black",command=lambda i=i :searchTheArchive(i)) #
        x.pack(side=TOP,fill=X)

    def on_closing():
        if messagebox.askokcancel("Quit HeadFinder?", "Do you want to quit?"):
            root.destroy()
    root.protocol("WM_DELETE_WINDOW", on_closing)

    root.mainloop()

()





#uses archiveSearch and makes a little GUI
from tkinter import *
import tkinter as tk
import threading
from tkinter import messagebox
from webScraper import *
import webScraper
import player
import time
import favoriteManager

def clear_lists():#makes it so user can click on multiple years
    item_name.clear()
    item_text.clear()
    ()

def set_thread_target(LINK):
    thread = threading.Thread(target=player.playSong(LINK))
    thread.daemon = True
    thread.start()
    ()



def run():
    # begin GUI stuff
    root = tk.Tk()
    root.title('HeadFinder')

    root.geometry("300x832")
    root.iconbitmap(default='favicon.ico')  # adds favicon
    root.resizable(width=False,height=False)


    def get_show_details(URL,set_title):
        setlist_details_window = Toplevel(root)
        setlist_details_window.iconbitmap(r'favicon.ico')  # adds favicon
        setlist_details_window.title(set_title)
        setlist_details_window.geometry("340x790")
        setlist_details_window.resizable(width=False,height=True)
        webScraper.get_setlist_and_mp3s("http://archive.org/details/" + URL)
        #player.stopall()

       # y = Button(setlist_details_window, text="pause", bg="red", command=player.stopall())
       # y.pack(side=TOP, fill=X)
        for i in range(0, len(set_list)):
            x = Button(setlist_details_window, text=str(set_list[i]), bg="slate gray", fg="black",command=lambda i=i: set_thread_target(set_mp3s[i]))
            x.pack(side=TOP, fill=X)


    ()


    def searchTheArchive(year):#searches the archive looking for a shows in a certian year
        year_window = Toplevel(root)
        year_window.iconbitmap(r'favicon.ico')  # adds favicon
        year_window.geometry("340x790")
        clear_lists()
        webScraper.find_item(year)
        webScraper.findTitle(year)

        year_window.resizable(width=False, height=False)

        canvas = tk.Canvas(year_window)
        scrolly = tk.Scrollbar(year_window, orient='vertical', command=canvas.yview)

        # display labels in the canvas
        canvas.config(width=318, height=840)
        num_items = len(item_text)
        for i in range(num_items):

            label = tk.Button(canvas, text=item_name[i], bg="OliveDrab",command=lambda i=i :get_show_details(item_text[i],item_name[i]))
            label.configure(width=45)
            canvas.create_window(0, i * 25, anchor='nw', window=label, height=25)

        canvas.configure(scrollregion=canvas.bbox('all'), yscrollcommand=scrolly.set)

        canvas.pack(fill='x', expand=True, side='left')
        scrolly.pack(fill='y', side='right',expand=True)

        root.mainloop()


        ()



    def open_favs():
        new_window= Toplevel(root)
        new_window.iconbitmap(r'favicon.ico')#adds favicon
        new_window.geometry("300x832")
        x=Button(new_window,text="Your favorites will be here eventually!", bg="indian red", command=favoriteManager.printFavorites())
        x.pack(side=TOP, fill=X)
    ()

    fav_button = Button(root, text="Favorites", bg="indian red", command=open_favs)
    fav_button.pack(side=TOP, fill=X)

    for i in range(1965,1996):
        x=str(i)
        x=Button(root,text=x,bg="NavajoWhite3",fg="black",command=lambda i=i :searchTheArchive(i)) #
        x.pack(side=TOP,fill=X)




    def on_closing():
        if messagebox.askokcancel("Quit HeadFinder?", "Do you want to quit?"):
            root.destroy()
            player.stopall()
    root.protocol("WM_DELETE_WINDOW", on_closing)

    threadtwo = threading.Thread(target=root.mainloop())
    threadtwo.daemon = True
    threadtwo.start()
  #  root.mainloop()
    ()
()


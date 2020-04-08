import time
from sqlite3.dbapi2 import Time

import webScraper
favorite_URLS = []
favorite_titles = []

def printFavorites():
    for i in range (0, len(favorite_URLS)):
        print (favorite_URLS[i])

    ()

def remove_item(name,link):
    favorite_URLS.clear()
    favorite_titles.clear()

    getFavsFromTXT()


    for  y in range (0, len(favorite_URLS)):
       if(str(favorite_URLS[y]).replace("\n","") == link):
            favorite_URLS.pop(y)
            favorite_titles.pop(y)

    f = open("names.txt", "w")
    for x in range (0, len(favorite_titles)):
        print(favorite_titles[x])
        f.write(favorite_titles[x]+"\n");
    f.close()

    f = open("links.txt", "w")
    for x in range(0, len(favorite_URLS)):

        f.write(favorite_URLS[x] + "\n");
    f.close()

    getFavsFromTXT()







def add_Favorites(set_name, set_link):
    f=open("links.txt","a")
    f.write(set_link+"\n");

    f.close()

    f=open("names.txt","a")
    f.write(set_name+"\n")
    f.close()

def getFavsFromTXT():
    favorite_URLS.clear()
    favorite_titles.clear()
    f=open("links.txt","r")
    for y in f.readlines():
        favorite_URLS.append(y.replace("\n",""))
    f.close()

    f1=open("names.txt","r")
    for x in f1.readlines():
        favorite_titles.append(x.replace("\n",""))
    f1.close

def get_favorite_URL(x):
    return favorite_URLS[x]

def get_favorite_title(x):
    return favorite_titles[x]

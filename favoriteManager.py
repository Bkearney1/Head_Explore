import webScraper
favorite_URLS = []
favorite_titles = []

def printFavorites():
    for i in range (0, len(favorite_URLS)):
        print (favorite_URLS[i])

    ()

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

def remove_from_favorites(URL):
    favorite_URLS.remove(URL)
    ()

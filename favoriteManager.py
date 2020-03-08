import webScraper
favorite_URLS = ["https://archive.org/details/gd1975-06-17.aud.unknown.87560.flac16","https://archive.org/details/gd1975-06-17.aud.unknown.87560.flac16","https://archive.org/details/gd1975-06-17.aud.unknown.87560.flac16"]

def printFavorites():
    for i in range (0, len(favorite_URLS)):
        print (favorite_URLS[i])
    print("this is a proof of concept.... will eventually be nicer with GUI integration and webscraping")
    ()


def add_favorites(URL):
    favorite_URLS.append(URL)
    ()


def remove_from_favorites(URL):
    favorite_URLS.remove(URL)
    ()

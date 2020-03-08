import requests
from bs4 import BeautifulSoup
#this file finds the title and link to all shows from a certian year
#populates global arrays item_text and "item_name"
item_name= []
item_text = []
set_list = []
set_mp3s = []

def findTitle(year):

    URL='https://archive.org/advancedsearch.php?q=collection%%3A%%28GratefulDead%%29+AND+date%%3A%%5B%d-01-01+TO+%d-12-31%%5D&fl%%5B%%5D=title&sort%%5B%%5D=date+asc&sort%%5B%%5D=&sort%%5B%%5D=&rows=10000&page=1&callback=callback&output=xml#raw'%(year,year)
    result = requests.get(URL)

    # check that archive.org isnt down
    if (result.status_code != 200):
        print('Something broke! please email: bkearney1@ycp.edu for some help! (archive.org is probably down)')
        # TODO:improve error checking, add mailto link s



    xml_doc = result.content
    soup = BeautifulSoup(xml_doc,"html.parser")
    for item in soup.findAll('doc'):
        item_name.append(''.join(item.findAll(text=True)))

    for i in range (0,len(item_name)):
        item_name[i] = item_name[i].replace('Grateful Dead Live at ','')
        item_name[i] = item_name[i].strip("\n")

()
def find_item(year):

    URL2='https://archive.org/advancedsearch.php?q=collection%%3A%%28GratefulDead%%29+AND+date%%3A%%5B%s-01-01+TO+%s-12-31%%5D&fl%%5B%%5D=identifier&sort%%5B%%5D=date+asc&sort%%5B%%5D=&sort%%5B%%5D=&rows=1000&page=1&callback=callback&output=xml'%(year,year)
    result2 = requests.get(URL2)

    xml_doc2 = result2.content
    soup2 = BeautifulSoup(xml_doc2, "html.parser")
    for item in soup2.findAll('doc'):
        item_text.append(''.join(item.findAll(text=True)))


    for i in range (0,len(item_text)):
        item_text[i] = item_text[i].strip("\n")


()


def get_setlist_and_mp3s (URL):
    set_mp3s.clear()
    set_list.clear()
    result3 = requests.get(URL)
    xml_doc1 = result3.content
    soup = BeautifulSoup(xml_doc1, "html.parser")
    counter=0
    for item in soup.findAll("link", {"itemprop": "associatedMedia"}):
        if (counter %2==0):
            set_mp3s.append(str(item))
        counter=counter+1

    for i in range (0,len(set_mp3s)):
        set_mp3s[i]=set_mp3s[i].strip("\" itemprop=\"associatedMedia\"/>")
        set_mp3s[i] = set_mp3s[i].replace("<link href=\"","")


    for item in soup.findAll("meta", {"itemprop": "name"}):
        set_list.append(str(item))


    for i in range (0,len(set_list)):
        set_list[i] = set_list[i].replace("<meta content=\"", "") #
        set_list[i] = set_list[i].replace(" &gt;\" itemprop=\"name\"/>","")
        set_list[i] = set_list[i].replace("\" itemprop=\"name\"/>","")
        set_list[i] = set_list[i].replace("-&gt;","")
        set_list[i] = set_list[i].replace("&gt;", "")
        set_list[i] = set_list[i].replace("//", "")

    ()
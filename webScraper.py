import requests
from bs4 import BeautifulSoup
#this file finds the title and link to all shows from a certian year
#populates global arrays item_text and "item_name"
item_name= []
item_text = []
def findTitle(year):

    URL='https://archive.org/advancedsearch.php?q=collection%%3A%%28GratefulDead%%29+AND+date%%3A%%5B%d-01-01+TO+%d-12-31%%5D&fl%%5B%%5D=title&sort%%5B%%5D=date+asc&sort%%5B%%5D=&sort%%5B%%5D=&rows=10000&page=1&callback=callback&output=xml#raw'%(year,year)
    result = requests.get(URL)

    # check that archive.org isnt down
    if (result.status_code != 200):
        print('Something broke! please email: bkearney1@ycp.edu for some help! (archive.org is probably down)')
        # TODO:improve error checking, add mailto link s



    xml_doc = result.content
    soup = BeautifulSoup(xml_doc,"html.parser")
    for potato in soup.findAll('doc'):
        item_name.append(''.join(potato.findAll(text=True)))

    for i in range (0,len(item_name)):
        item_name[i] = item_name[i].replace('Grateful Dead Live at ','')
        item_name[i] = item_name[i].strip("\n")
()
def find_item(year):

    URL2='https://archive.org/advancedsearch.php?q=collection%%3A%%28GratefulDead%%29+AND+date%%3A%%5B%s-01-01+TO+%s-12-31%%5D&fl%%5B%%5D=identifier&sort%%5B%%5D=date+asc&sort%%5B%%5D=&sort%%5B%%5D=&rows=1000&page=1&callback=callback&output=xml'%(year,year)
    result2 = requests.get(URL2)

    xml_doc2 = result2.content
    soup2 = BeautifulSoup(xml_doc2, "html.parser")
    for potato2 in soup2.findAll('doc'):
        item_text.append(''.join(potato2.findAll(text=True)))


    for i in range (0,len(item_text)):
        item_text[i] = item_text[i].strip("\n")


()
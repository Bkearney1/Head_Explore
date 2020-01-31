import requests
from bs4 import BeautifulSoup

title_text= []
def findTitle(year):

    URL='https://archive.org/advancedsearch.php?q=collection%%3A%%28GratefulDead%%29+AND+date%%3A%%5B%d-01-01+TO+%d-12-31%%5D&fl%%5B%%5D=title&sort%%5B%%5D=date+asc&sort%%5B%%5D=&sort%%5B%%5D=&rows=1000&page=1&callback=callback&output=xml#raw'%(year,year)
    result = requests.get(URL)

    # check that archive.org isnt down
    if (result.status_code != 200):
        print('Something broke! please email: bkearney1@ycp.edu for some help! (archive.org is probably down)')
        # TODO:improve error checking, add mailto link s



    xml_doc = result.content
    soup = BeautifulSoup(xml_doc,"html.parser")
    for potato in soup.findAll('doc'):
        title_text.append(''.join(potato.findAll(text=True)))

    for i in range (0,len(title_text)):
        title_text[i] = title_text[i].replace('Grateful Dead Live at ','')

        title_text[i] = title_text[i].strip("\n")






    return title_text
()

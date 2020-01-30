import requests
from bs4 import BeautifulSoup


def findTitle(year):

    URL='https://archive.org/advancedsearch.php?q=collection%%3A%%28GratefulDead%%29+AND+date%%3A%%5B%d-01-01+TO+%d-12-31%%5D&fl%%5B%%5D=title&sort%%5B%%5D=date+asc&sort%%5B%%5D=&sort%%5B%%5D=&rows=1000&page=1&callback=callback&output=xml#raw'%(year,year)
    result = requests.get(URL)

    # check that archive.org isnt down
    if (result.status_code != 200):
        print('Something broke! please email: bkearney1@ycp.edu for some help! (archive.org is probably down)')
        # TODO:improve error checking, add mailto link s

    xml_doc = result.content
    soup = BeautifulSoup(xml_doc,"html.parser")
    html_titles=str(soup.find_all('doc'))

    #TODO add show titles to a data structure
    #clean the HTML off
    html_titles=html_titles.replace('<doc>','')
    html_titles = html_titles.replace('</doc>', '')
    html_titles = html_titles.replace('</str>', '')
    html_titles = html_titles.replace('<str name="title">', '')
    html_titles = html_titles.replace('[','')
    html_titles = html_titles.replace(']', '')

    print(html_titles)
()

import requests
from bs4 import BeautifulSoup

def findTitle():
    URL= 'https://archive.org/details/gd89-10-19.nak.rob_r.7595.sbefail.shnf'
    request=requests.get(URL)

    #check that archive.org isnt down
    if (request.status_code==404):
        print('Something broke! please email: bkearney1@ycp.edu for some help!')
        #TODO:improve error code finding, add mailto link

    raw_page=request.text
    soup= BeautifulSoup(raw_page, features="html.parser")

    concert_title=soup.find('h1')

    pretty_string= concert_title.get_text()

    print(pretty_string)

    return pretty_string
()
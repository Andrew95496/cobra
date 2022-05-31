# Built-in scrape function

from dataclasses import dataclass
from datetime import datetime
import requests
from bs4 import BeautifulSoup

from Objects import cobra_request_object

# * USEFUL methods

# res.elapsed
#  res.headers
# 


@dataclass
class Scraper:
    
    def __init__(self,url,element,element_name,filename,find_all = True ):
                self.url = url
                self.element = element
                self.element_name = element_name
                self.filename = filename
                self.find_all = find_all

    def simple_scrape(self): # using the initial parameters run a web scrape process
        res = requests.get(self.url)
        src = res.content
        html = BeautifulSoup(src, 'lxml')
        results = html.findAll(f'{self.element}')
        user_request = cobra_request_object.Cobra_Request(res.status_code, results, res.elapsed)
        return repr(user_request)

    def advanced_scrape():
        pass

    def python(): # complies the code into python #! MIGHT MAKE THIS IS OWN FOLDER
        pass
k



if __name__ == '__main__':
    x = Scraper('https://www.bjjheroes.com/a-z-bjj-fighters-list',
    'div', 'home', 'zzz')
    print(x.simple_scrape())

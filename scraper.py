# Built-in scrape function

from dataclasses import dataclass
from datetime import datetime
import requests
from bs4 import BeautifulSoup

from Objects import *
import Objects
from Objects import cobra_request_object
from Objects.memory_object import Memory

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

    # add data to memory
    def save_to_memory(self, Data):
        user_data = Memory('0xF372AD', Data, '12:30:3473828')

        with open('.memory', 'a') as scraped_data: #! MAKE FILE READ/WRITE A MODULE
            scraped_data.write(repr(user_data))
        return repr(user_data)

    def simple_scrape(self): # using the initial parameters run a web scrape process
        res = requests.get(self.url)
        src = res.content
        html = BeautifulSoup(src, 'lxml')
        results = html.find(f'{self.element}')
        user_request = cobra_request_object.Cobra_Request(res.status_code, results, res.elapsed)
        self.save_to_memory(results)
        return repr(user_request)

    def advanced_scrape():
        pass
    
    
        

    def python(): # complies the code into python #! MIGHT MAKE THIS IS OWN FOLDER
        pass




if __name__ == '__main__':
    x = Scraper('https://www.bjjheroes.com/a-z-bjj-fighters-list',
    'table', 'home', 'zzz')
    data = x.simple_scrape()
    print(data)
    

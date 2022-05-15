# Built-in scrape function will take in kwargs

from dataclasses import dataclass
from datetime import datetime

@dataclass
class Scraper:
    
    def __init__(self,url,element,element_name,filename,find_all = True ):
                self.url = url
                self.element = element
                self.element_name = element_name
                self.filename = filename
                self.find_all = find_all

    def scrape(): # using the initial parameters run a web scrape process
        pass

    def python(): # complies the code into python #! MIGHT MAKE THIS IS OWN FOLDER
        pass
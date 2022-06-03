# Built-in scrape function

from dataclasses import dataclass
from datetime import datetime
import requests
from bs4 import BeautifulSoup
import pandas as pd
import hashlib


from Objects import cobra_request_object
from Objects.file_object import File
from Objects.memory_object import Memory

# * USEFUL methods

# res.elapsed
#  res.headers
# 

@dataclass
class Scraper:
    # Initializing the scraper object. URL is the only non optional parameter.
    # @param url: specific url of the site you want to be scraped
    # @param filename: name you want your file(s) to be saved as
    # @param type: type of object to create [ table | image | url ]
    # @param extension: file extension to create Default: xlsx
    # @param find_all: Find all table in url
    def __init__(self,url,filename = None ,type = 'table',extension = 'xlsx',find_all = True ):
                self.url = url
                self.filename = filename
                self.type = type
                self.extension = extension
                self.find_all = find_all

    # add data to memory
    def save_to_memory(self, raw_data, data):
        hash = hashlib.new('sha256')
        raw_data = f'{raw_data}{data}'
        raw_data_binary = raw_data.encode('utf-8')
        hash.update(raw_data_binary)
        address = hash.hexdigest() # Using hashlib to create a unique address for the data in memory
        user_data = Memory(address, raw_data, data, datetime.now()) # User data memory object #* Objects/memory_object.py
        saved_memory = File('.memory', 'a') # sends dataframe and raw data to memory #* Objects/file_object.py
        saved_memory.write(repr(user_data))
        return repr(user_data) # returns a representation of the Memory Object

    
    def simple_scrape(self): # using the initial parameters run a web scrape process
        res = requests.get(self.url)
        src = res.content
        html = BeautifulSoup(src, 'lxml')
        results = html.findAll(f'{self.type}')
        tables = pd.read_html(str(results)) # turn results into a list of tables
        user_request = cobra_request_object.Cobra_Request(res.status_code, tables, res.elapsed) # place data into a request object
        for table in tables: # loop through the tables list write it to a file
            if self.filename == None:
                saved_file  = File(f'Test/file_{datetime.now()}.{self.extension}', 'w')
                saved_file.write_excel(table)
                print('file created')
            self.save_to_memory(0, table) 
        print(f'Data Tables Found: {len(tables)}')
        return user_request

    def advanced_scrape():
        pass
    
    
        

    def python(): # complies the code into python #! MIGHT MAKE THIS IS OWN FOLDER
        pass




if __name__ == '__main__':
    x = Scraper('https://en.wikipedia.org/wiki/Computer_science')
    data = x.simple_scrape()
    y = Scraper('https://en.wikipedia.org/wiki/Miami_Dolphibs')
    data = y.simple_scrape()
    z= Scraper('https://en.wikipedia.org/wiki/science')
    data = z.simple_scrape()
    a = Scraper('https://en.wikipedia.org/wiki/nfl')
    data = a.simple_scrape()
    # print(repr(data))

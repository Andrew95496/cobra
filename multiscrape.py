# Built-in scrape function
import os
import threading
import time
import itertools as its
from dataclasses import dataclass
from datetime import datetime
from numpy import append
import requests
from bs4 import BeautifulSoup
import pandas as pd
import hashlib
from numba import jit

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

    def __create_address(self, raw_data, data):
        hash = hashlib.new('sha256')
        raw_data = f'{raw_data}{data}'
        raw_data_binary = raw_data.encode('utf-8')
        hash.update(raw_data_binary)
        address = hash.hexdigest() # Using hashlib to create a unique address for the data in memory
        return address

    # add data to memory
    def save_to_memory(self, raw_data, data):
        address = self.__create_address(raw_data, data)
        append_address = File('State/.address')
        address_list = append_address.read()
        if address not in address_list:
            append_address.append(f'{address}\n')
            user_data = Memory(address, raw_data, data, datetime.now()) # User data memory object #* Objects/memory_object.py
            saved_memory = File('.memory') # sends dataframe and raw data to memory #* Objects/file_object.py
            saved_memory.append(repr(user_data))
        else:
            print('CONTENT ALREADY IN MEMORY')
        return None # returns a representation of the Memory Object

    def __write_to_file(self, data):
        saved_file  = File(f'Test/file_{datetime.now()}.{self.extension}')
        saved_file.write_excel(data)


    def simple_scrape(self): # using the initial parameters run a web scrape process
        threads = []
        res = requests.get(self.url)
        src = res.content
        html = BeautifulSoup(src, 'lxml')
        results = html.findAll(f'{self.type}')
        tables = pd.read_html(str(results), encoding=f'{res.encoding}') # turn results into a list of tables
        user_request = cobra_request_object.Cobra_Request(res.status_code, tables, res.elapsed) # place data into a request object
        start = time.perf_counter()
        for table in tables: # loop through the tables list write it to a file
            if self.filename == None:
                t = threading.Thread(target=self.__write_to_file, args=[table])
                t.start()
                threads.append(t)
        for thread in threads:
            thread.join()
        end = time.perf_counter()
        print(end - start)
                # saved_file.write_excel(table)
        self.save_to_memory(0, tables) 
        print(f'Data Tables Found: {len(tables)}')
        return user_request

    def advanced_scrape():
        pass

    def compile_to_python(self): # complies the code into python #! NOT ACTUALLY COMPILING
        code = f'''
import requests
from bs4 import BeautifulSoup
import pandas as pd


res = requests.get('{self.url}')
src = res.content
html = BeautifulSoup(src, 'lxml')
results = html.findAll(f'{self.type}')
tables = pd.read_html(str(results), encoding=f'{{res.encoding}}')
count = 0
for table in tables: # loop through the tables list write it to a file
        with open(f'file_{{count}}.xlsx') as file:
            file.write(table)
        count += 1
        '''
        SOURCE_CODE = File('Compile_Test/compiled_cobra.py')
        SOURCE_CODE.write(code)




if __name__ == '__main__':
    x = Scraper('https://en.wikipedia.org/wiki/Computer_science')
    data = x.simple_scrape()
    y = Scraper('https://en.wikipedia.org/wiki/Miami_Dolphins')
    data = y.simple_scrape()
    z= Scraper('https://en.wikipedia.org/wiki/Baltimore_Ravens')
    data = z.simple_scrape()
    a = Scraper('https://en.wikipedia.org/wiki/nfl')
    data = a.simple_scrape()
    a.compile_to_python()


    M = Memory()

    # M.DUMP_ALL()


    # print(repr(data))
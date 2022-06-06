import os
import threading
import time
from dataclasses import dataclass
from datetime import datetime

# Web Scraping 
import requests
from bs4 import BeautifulSoup
import hashlib
import shutil

# Dataframes
import pandas as pd

# Image Matrix
from PIL import Image
from numpy import array

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

    def __write_to_file(self, data, content_type):
        saved_file  = File(f'Test/file_{datetime.now()}.{self.extension}')
        if content_type.find('text') != -1:
            saved_file.write_excel(data)
        else:
            saved_file.write(str(data))

    def __download_img(self, response, filename):
        with open(filename, 'wb') as img:
                shutil.copyfileobj(response.raw, img)
        return img


    def __img_to_marix(self, filename):
        img = Image.open(filename)
        matrix = array(img)
        return matrix

    def SMP_table_scrape(self): # using the initial parameters run a web scrape process
        threads = []
        res = requests.get(self.url)
        content_type = res.headers['Content-Type']
        src = res.content
        html = BeautifulSoup(src, 'lxml')
        results = html.findAll(f'{self.type}')
        tables = pd.read_html(str(results), encoding=f'{res.encoding}') # turn results into a list of tables
        user_request = cobra_request_object.Cobra_Request(res.status_code, tables, res.elapsed) # place data into a request object
        start = time.perf_counter()
        for table in tables: # loop through the tables list write it to a file
            if self.filename == None:
                t = threading.Thread(target=self.__write_to_file, args=[table, content_type])
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

    def ADV_table_scrape():
        pass

    def SMP_img_scrape(self):
        threads = []
        res = requests.get(self.url)
        src = res.content
        html = BeautifulSoup(src, 'lxml')
        images = html.findAll(f'img')
        user_request = cobra_request_object.Cobra_Request(res.status_code, images, res.elapsed) # place data into a request object
        start = time.perf_counter()
        for image in images[1:]: # loop through the tables list write it to a file
            url = image.attrs['src']
            response = requests.get(url, stream=True)
            filename = f'Test/{datetime.now()}.jpg'
            content_type = response.headers['Content-Type']
            self.__download_img(response, filename)
            matrix = self.__img_to_marix(filename)
            if self.filename == None:
                t = threading.Thread(target=self.__write_to_file, args=[matrix, content_type])
                t.start()
                threads.append(t)
        for thread in threads:
            thread.join()
        end = time.perf_counter()
        print(end - start)
        print(f'Images Found: {len(images)}')
        return user_request

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
    # x = Scraper('https://en.wikipedia.org/wiki/Computer_science')
    # data = x.SMP_table_scrape()
    # y = Scraper('https://en.wikipedia.org/wiki/Miami_Dolphins')
    # data = y.SMP_table_scrape()
    # z= Scraper('https://en.wikipedia.org/wiki/Baltimore_Ravens')
    # data = z.SMP_table_scrape()
    a = Scraper('https://en.wikipedia.org/wiki/nfl')
    data = a.SMP_table_scrape()
    # a.compile_to_python()

    img = Scraper('https://www.google.com/search?q=google&sxsrf=ALiCzsa-QwM3tL-xS-jwzHaXehKYQJbHwA:1654465152283&source=lnms&tbm=isch&sa=X&ved=2ahUKEwigscf9opf4AhXDZzABHVfODAUQ_AUoBHoECAIQBg&biw=1440&bih=821&dpr=2', extension='txt')
    img.SMP_img_scrape()


    # M.DUMP_ALL()


    # print(repr(data))
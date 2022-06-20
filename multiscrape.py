import threading
from dataclasses import dataclass
from datetime import datetime
import dis

# Web Scraping
import requests
from bs4 import BeautifulSoup
import hashlib
# import shutil

# Dataframes
import pandas as pd

# Image Matrix
from PIL import Image
from numpy import array

from Objects import cobra_request_object
from Objects.file_object import File
from Objects.memory_object import Memory
from Objects.plot_object import Plot

# * USEFUL methods

# res.elapsed
# res.headers



@dataclass
class Scraper:
    # Initializing the scraper object. URL is the only non optional parameter.
    # @param url: specific url of the site you want to be scraped
    # @param filename: name you want your file(s) to be saved as
    # @param type: type of object to create [ table | image | url ]
    # @param extension: file extension to create Default: xlsx
    # @param find_all: Find all table in url

    __slots__ = ('url', 'filename', 'type', 'extension', 'find_all')
    def __init__(
                self, 
                url, 
                filename=None,
                type='table',
                extension='xlsx',
                find_all=True):

        self.url = url
        self.filename = filename
        self.type = type
        self.extension = extension
        self.find_all = find_all

    def __create_address(self, raw_data, data):
        hash = hashlib.new('sha256')
        raw_data = f'{raw_data}{data}'
        raw_data_binary = raw_data.encode('utf-8')
        hash.update(raw_data_binary)                                    # Using hashlib to create a unique address for the data in memory
        address = hash.hexdigest()
        return address

    # add data to memory
    def save_to_memory(self, raw_data, data):
        address = self.__create_address(raw_data, data)
        append_address = File('State/.address')
        address_list = append_address.read()
        if address not in address_list:
            append_address.append(f'{address}\n')
            user_data = Memory(address, raw_data, data, datetime.now())  # User data memory object #* Objects/memory_object.py
            saved_memory = File('.memory')                               # sends Dataframe and raw data to memory #* Objects/file_object.py
            saved_memory.append(str(user_data))
        else:
            print('CONTENT ALREADY IN MEMORY')
        return None                                                      # returns a representation of the Memory Object

    def __write_to_file(self, data, content_type):
        saved_file = File(f'Test/file_{datetime.now()}.{self.extension}')
        if content_type.find('text') != -1:
            saved_file.write_excel(data)
        else:
            saved_file.write(str(data))

    # def __download_img(self, response, filename):
    #     with open(filename, 'wb') as img:
    #         shutil.copyfileobj(response.raw, img)
    #     return img

    # def __img_to_matrix(self, filename):
    #     img = Image.open(filename)
    #     matrix = array(img)
    #     return matrix
    
    def SMP_table_scrape(self):                                           # using the initial parameters run a web scrape process
        threads = []
        res = requests.get(self.url)
        content_type = res.headers['Content-Type']
        src = res.content
        html = BeautifulSoup(src, 'lxml')
        results = html.findAll(f'{self.type}')
        # turn results into a list of tables                              # if the scrape returns none exit code
        try:
            tables = pd.read_html(str(results))
        except ValueError:
            print(f'NO TABLES FOUND')
            return None
        user_request = cobra_request_object.Cobra_Request(                # place data into a request object
            res.status_code, 
            {f'table{num + 1}': table for num, table in enumerate(tables)}, 
            len(tables),
            res.elapsed)

        for table in tables:                                              # loop through the tables list write it to a file
            if self.filename == None:
                t = threading.Thread(target=self.__write_to_file, 
                                    args=[table, content_type])           # Multithreading the file writing process
                t.start()
                threads.append(t)
        for thread in threads:
            thread.join()
        self.save_to_memory(0, tables)                                     # saved_file.write_excel(table)
        print(f'Data Tables Found: {len(tables)}')
        return user_request

    def ADV_table_scrape():
        pass

    # def SMP_img_scrape(self):
    #     threads = []
    #     res = requests.get(self.url)
    #     src = res.content
    #     html = BeautifulSoup(src, 'lxml')
    #     images = html.findAll(f'img')
    #     user_request = cobra_request_object.Cobra_Request(
    #         res.status_code, images, res.elapsed)                          # place data into a request object
    #     start = time.perf_counter()
    #     for image in images[1:]:                                           # loop through the tables list write it to a file
    #         url = image.attrs['src']
    #         response = requests.get(url, stream=True)
    #         filename = f'Test/{datetime.now()}.jpg'
    #         content_type = response.headers['Content-Type']
    #         self.__download_img(response, filename)
    #         matrix = self.__img_to_marix(filename)
    #         if self.filename == None:
    #             t = threading.Thread(target=self.__write_to_file,
    #                                 args=[matrix, content_type])
    #             t.start()
    #             threads.append(t)
    #     for thread in threads:
    #         thread.join()
    #     end = time.perf_counter()
    #     print(end - start)
    #     print(f'Images Found: {len(images)}')
    #     return user_request

    # complies the code into python #! NOT ACTUALLY COMPILING
    def compile_to_python(self):
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
    x = Scraper('https://en.wikipedia.org/wiki/ADCC_Submission_Fighting_World_Championship')
    data = x.SMP_table_scrape()
    i = data.contents
    for key, value in i.items():
        i[key] = value.astype('category')
    plot = Plot(i)
    plot.create_view()
    
    # DUMP = Memory()
    # DUMP.DUMP_ALL()
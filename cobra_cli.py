import argparse
import pprint

import requests

from multiscrape import Scraper




parser = argparse.ArgumentParser(description='Multithreaded Command Line Data Engine to collect Dataframes from the Internet')

parser.add_argument('url', help='specific URL you want to scrape')
parser.add_argument('--filename',  default='cobra_data', help='name of file that will store the data')
parser.add_argument('--extension', default= 'xlsx', help='file type')
parser.add_argument('--findall', default='true', help='find all Dataframes on the webpage')
args = parser.parse_args()


def Cobra():
    request = Scraper(url= args.url, filename= args.filename, extension= args.extension, find_all= args.findall ,type='table' )
    request.SMP_table_scrape()


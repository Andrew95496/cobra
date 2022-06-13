import argparse
import pprint

import requests

from multiscrape import Scraper




parser = argparse.ArgumentParser(description='Multithreaded Command Line Data Engine to collect Dataframes from the Internet',
                                epilog='Report Issues: https://github.com/Andrew95496/cobra/issues')

#* STANDARD ARGUMENTS
parser.add_argument('url', help='specific URL you want to scrape') 

#! OPTIONAL STANDARD ARGUMENTS
parser.add_argument('--filename',  default='cobra_data', help='name of file that will store the data')
parser.add_argument('--extension', default= 'xlsx', help='file type')
parser.add_argument('--findall', default='true', help='find all Dataframes on the webpage')

# OPTIONAL ARGUMENTS
parser.add_argument('-meta', help='show metadata from the scrape')
parser.add_argument('-viz', help='visualize metadata')
# parser.add_argument()
# parser.add_argument()
# parser.add_argument()
# parser.add_argument()
# parser.add_argument()
# parser.add_argument()
# parser.add_argument()
# parser.add_argument()
# parser.add_argument()
# parser.add_argument()
# parser.add_argument()
# parser.add_argument()

args = parser.parse_args()


def Cobra():
    # TODO: use the COBRA REQUEST OBJECT to be used by other parts of the program
    request = Scraper(url= args.url, filename= args.filename, extension= args.extension, find_all= args.findall ,type='table' )
    request.SMP_table_scrape()


from dataclasses import dataclass
from datetime import datetime
"""
Cobra Request Object - Information about a scrape will be stored in the request object
# Returned by all scraper functions in ../ multiscrape.py
"""

@dataclass
class Cobra_Request:

    __slots__ = ('response', 'contents', 'metadata', 'init', 'runtime')

    def __init__(self, response, contents, metadata, runtime):
        self.response = response
        self.contents = contents
        self.metadata = metadata
        self.init = datetime.now()
        self.runtime = runtime

    def __str__(self) -> str:
        request_object = f'''Initialization: {self.init}\n
Response: {self.response}\n
Contents: {self.contents}\n
Metadata: {self.metadata}
Runtime: {self.runtime}\n
        '''
        return request_object
    


if __name__ == '__main__':

    x = Cobra_Request('200', '<span class="search-highlight">WU Poster LaTeX Template</span>', 'NULL', '2.000')
    
    print(x.__slots__.__sizeof__())
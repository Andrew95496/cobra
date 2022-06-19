from dataclasses import dataclass
from datetime import datetime

@dataclass
class Cobra_Request:

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

    x = Cobra_Request('200', '<span class="search-highlight">WU Poster LaTeX Template</span>')
    
    print(x)
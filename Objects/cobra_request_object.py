from dataclasses import dataclass
from datetime import datetime

@dataclass
class Cobra_Request:

    def __init__(self, response, contents, runtime):
        self.response = response
        self.contents = contents
        self.init = datetime.now()
        self.runtime = runtime

    def __repr__(self):
        rep = f'''Initialization: {self.init}\n
Response: {self.response}\n
Contents: {self.contents}\n
Runtime: {self.runtime}\n
        '''
        return rep

if __name__ == '__main__':

    x = Cobra_Request('200', '<span class="search-highlight">WU Poster LaTeX Template</span>')
    
    print(x)
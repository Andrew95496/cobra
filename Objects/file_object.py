from dataclasses import dataclass
import itertools as its
@dataclass
class File:
    
    def __init__(self, filename):
        self.filename = filename

    def append(self, data):
        with open(f'{self.filename}', 'a') as file: 
            file.write(data)

    def write(self, data):
        with open(f'{self.filename}', 'w') as file: 
            file.write(data)
        
    def write_excel(self, data):
        data.to_excel(f'{self.filename}')
        # print(f'{self.filename}')

    def read(self):
        with open(f'{self.filename}', 'r') as file:
            LINES = [line.rstrip('\n') for line in file] 
        return LINES
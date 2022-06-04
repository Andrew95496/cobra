from dataclasses import dataclass
import pandas

@dataclass
class File:
    
    def __init__(self, filename):
        self.filename = filename

    def write(self, data):
        with open(f'{self.filename}', 'a') as file: 
            file.write(data)
        
    def write_excel(self, data):
        data.to_excel(f'{self.filename}.xlsx')
        print(f'{self.filename}')

    def read(self):
        LINES = []
        with open(f'{self.filename}', 'r') as file: 
            for line in file:
                line = line.rstrip('\n')
                LINES.append(line)
        return LINES
from dataclasses import dataclass
import pandas

@dataclass
class File:
    
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def write(self, data):
        with open(f'{self.filename}', f'{self.mode}') as file: 
            file.write(data)
        
    def write_excel(self, data):
        data.to_excel(f'{self.filename}.xlsx')

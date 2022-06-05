from dataclasses import dataclass


@dataclass
class Memory:

    def __init__(self, address=None, raw_data=None, data=None, initialization=None):
        self.address = address
        self.raw_data = raw_data
        self.data = data
        self.initialization = initialization

    def __repr__(self) -> str:
        rep = f'''Address: {self.address}\nRaw Contents: {self.raw_data}\nContents:\n{self.data}\nTime: {self.initialization}\n'''
        return rep

    def DUMP_ALL(self):
        with open('.memory', 'w') as MEMORY, open('State/.address', 'w' ) as ADDRESS:
            ADDRESS.write('')
            MEMORY.write('')
        print('MEMORY DUMPED')
        

    def DUMP(self, address):
        return f'MEMORY DUMPED AT {address}'

    # get memory
    def get():
        pass
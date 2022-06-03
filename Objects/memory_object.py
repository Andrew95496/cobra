from dataclasses import dataclass


@dataclass
class Memory:

    def __init__(self, address, raw_data, data, initialization):
        self.address = address
        self.raw_data = raw_data
        self.data = data
        self.initialization = initialization

    def __repr__(self) -> str:
        rep = f'''Address: {self.address}\nRaw Contents: {self.raw_data}\nContents:\n{self.data}\nTime: {self.initialization}\n'''
        return rep

    # get memory
    def get():
        pass
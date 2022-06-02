from dataclasses import dataclass

@dataclass
class Memory:

    def __init__(self, address, data, initialization):
        self.address = address
        self.data = data
        self.initialization = initialization

    def __repr__(self) -> str:
        rep = f'''address: {self.address}\nContents: {self.data}\nTime: {self.initialization}\n'''
        return rep
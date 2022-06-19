from dataclasses import dataclass


@dataclass
class Data:
    
    __slots__ = ('contents')
    
    def __init__(self, contents):
        self.contents = contents
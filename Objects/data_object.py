from dataclasses import dataclass


@dataclass(slots=True)
class Data:
        
    def __init__(self, contents):
        self.contents = contents
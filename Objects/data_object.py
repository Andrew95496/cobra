from dataclasses import dataclass


@dataclass
class Data:

    def __init__(self, contents):
        self.contents = contents
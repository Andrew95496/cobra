from dataclasses import dataclass

@dataclass
class Cache:

    __slots__ = ('contents')

    def __init__(self, contents) -> None:
        self.contents = contents

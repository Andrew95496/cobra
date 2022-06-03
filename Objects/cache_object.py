from dataclasses import dataclass

@dataclass
class Cache:

    def __init__(self, contents) -> None:
        self.contents = contents

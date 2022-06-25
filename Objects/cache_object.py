from dataclasses import dataclass

@dataclass(slots=True)
class Cache:

    def __init__(self, contents) -> None:
        self.contents = contents

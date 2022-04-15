from dataclasses import dataclass
import datetime

@dataclass
class Entry:
    id: int
    name: str
    description: str
    cipher: str
    shift: int
    created_on: int
    last_modified_on: int


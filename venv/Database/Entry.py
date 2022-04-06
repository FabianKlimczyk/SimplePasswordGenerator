from dataclasses import dataclass
import datetime

@dataclass
class Entry:
    id: int
    name: str
    description: str
    password: str
    created_on: int
    last_modified_on: int


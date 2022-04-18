'''
----------------------------------------------------
[LogNo] [Date]      [Name]  [Description]
----------------------------------------------------
001     06-04-22    FKL     Create file
002     14-04-22    FKL     - change fieldname password to cipher
                            - add field shift
'''
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


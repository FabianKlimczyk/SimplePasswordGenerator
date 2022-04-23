'''
----------------------------------------------------
[LogNo] [Date]      [Name]  [Description]
----------------------------------------------------
001     06-04-22    FKL     Create file
002     14-04-22    FKL     - change fieldname password to cipher
                            - add field shift
003     21-02-22    FKL     - add field login
'''
from dataclasses import dataclass
import datetime

@dataclass
class Entry:
    id: int
    name: str
    login: str
    description: str
    cipher: str
    shift: int
    created_on: float
    last_modified_on: float


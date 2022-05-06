'''
----------------------------------------------------
[LogNo] [Date]      [Name]  [Description]
----------------------------------------------------
001     06-05-22    FKL     Create file
                            Add function:
                                - showData
                                - getPassword

This module manages the data from the database
'''

import sqlite3 as sql3
import time
from src.main.Database.DBMgt import getEntry
from src.main.Controller.DeEnCoding import decode

def showData(conn: sql3.Connection, where: str, value: str) -> None:
    data = list(getEntry(conn, where, value))
    for i in data:
        datalst = list(i)
        datalst[4] = '*****'  #pw
        datalst[5] = '*****'  #shift
        datalst[6] = time.ctime(datalst[6]) #created
        datalst[7] = time.ctime(datalst[7]) #modified
        print(datalst)

def getPassword(conn: sql3.Connection, where: str, value: str):
    data = list(getEntry(conn, where, value))
    for i in data:
        datalst = list(i)
        print(decode(datalst[4],datalst[5]))

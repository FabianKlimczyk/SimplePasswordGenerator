'''
----------------------------------------------------
[LogNo] [Date]      [Name]  [Description]
----------------------------------------------------
001     18-04-22    FKL     Create file
                            Add function:
                                - initDB
                                - setupTable
002     21-04-22    FKL     Add function:
                                - insertEntry
                                - update Entry
                                - deleteEntry
                                - getEntry

This module manages the database connection
'''

import sqlite3 as sql3
from src.main.Controller.FileMgt import getPath
from src.main.Utility.Strings import getString
import src.main.Model.Entry as entry

def setupTables() -> bool:
    dbfile = getPath(4)
    connection = sql3.connect(dbfile)
    crsr = connection.cursor()
    # Entries Table
    qry_create_entries = '''
        CREATE TABLE Entries (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(30),
        login VARCHAR(30),
        description VARCHAR(30),
        cipher VARCAHR(36),
        shift INTEGER,
        created_on REAL,
        last_modified_on REAL
        )
        '''
    try:
        crsr.execute(qry_create_entries)
        connection.commit()
        connection.close()
        print(getString("db_created", "DE"))
    except Exception as e:
        # Database already exists
        print(getString("db_ready", "DE"))



def insertEntry(Entry: entry.Entry):
    #TODO Prüfung ob name bereits vorhanden, verhindern doppelter Einträge
    dbfile = getPath(4)
    connection = sql3.connect(dbfile)
    crsr = connection.cursor()
    params = (Entry.name,Entry.login,Entry.description,Entry.cipher,Entry.shift,Entry.created_on,Entry.last_modified_on)
    qry_insert_entry = '''INSERT INTO Entries VALUES (Null, ?, ?, ?, ?, ?, ?, ?)'''
    crsr.execute(qry_insert_entry,params)
    connection.commit()

def updateEntry(name: str, columnname: str, newValue) -> bool:
    #TODO nur bestimmte Felder dürfen geändert werden
    dbfile = getPath(4)
    connection = sql3.connect(dbfile)
    crsr = connection.cursor()
    updateValues = (newValue, name)
    qry_update_entry = f'''UPDATE Entries SET {columnname} WHERE name = ?'''
    crsr.execute(qry_update_entry,updateValues)
    connection.commit()
    return True

def deleteEntry():
    #TODO implementieren
    pass

def getEntry(all: True) -> any:
    #TODO Ausgabe des Shifts "verpixeln"
    dbfile = getPath(4)
    connection = sql3.connect(dbfile)
    crsr = connection.cursor()
    qry_select_entry = "SELECT * FROM Entries"
    data = crsr.execute(qry_select_entry)
    return data

def init_DB():
    setupTables()



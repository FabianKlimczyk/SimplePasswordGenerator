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

def setupTables(conn: sql3.Connection) -> bool:
    crsr = conn.cursor()
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
        conn.commit()
        print(getString("db_created", "DE"))
    except Exception as e:
        # Database already exists
        print(getString("db_ready", "DE"))


def insertEntry(conn: sql3.Connection, Entry: entry.Entry):
    #TODO Prüfung ob name bereits vorhanden, verhindern doppelter Einträge
    crsr = conn.cursor()
    params = (Entry.name,Entry.login,Entry.description,Entry.cipher,Entry.shift,Entry.created_on,Entry.last_modified_on)
    qry_insert_entry = '''
    INSERT INTO Entries 
    VALUES (Null, ?, ?, ?, ?, ?, ?, ?)'''
    crsr.execute(qry_insert_entry,params)
    conn.commit()

def updateEntry(conn: sql3.Connection, name: str, columnname: str, newValue) -> bool:
    #TODO nur bestimmte Felder dürfen geändert werden
    crsr = conn.cursor()
    updateValues = (newValue, name)
    qry_update_entry = f'''
        UPDATE Entries 
        SET {columnname} 
        WHERE name = ?
    '''
    crsr.execute(qry_update_entry,updateValues)
    conn.commit()
    return True

def deleteEntryById(conn: sql3.Connection, id: str) -> bool:
    #TODO return Value in case it is possible or not
    crsr = conn.cursor()
    qry_delete_entry = '''
    DELETE FROM Entries 
    WHERE id = ?
    '''
    crsr.execute(qry_delete_entry, id)
    conn.commit()
    return True


def getEntry(conn: sql3.Connection, where: str, value: str) -> any:
    #TODO Ausgabe des Shifts "verpixeln"
    crsr = conn.cursor()
    qry_select_entry = '''
    SELECT * 
    FROM Entries'''
    if where != "" and value != "":
        where += "= ?"
        qry_select_entry = f'''
                SELECT * 
                FROM Entries
                WHERE {where}'''
    data = crsr.execute(qry_select_entry, value)
    return data

def getDatabaseConnection() -> sql3.Connection:
    dbfile = getPath(4)
    connection = sql3.connect(dbfile)
    return connection


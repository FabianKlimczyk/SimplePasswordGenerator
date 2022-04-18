import sqlite3 as sql3
from src.main.Controller.FileMgt import getPath
from src.main.Utility.Strings import getString

def setupTables(crsr: sql3.connect().cursor()) -> bool:
    qry_create_entries = '''
        CREATE TABLE Entries (
        id INTEGER PRIMARY KEY,
        name VARCHAR(30),
        login VARCHAR(30),
        cipher VARCAHR(36),
        shift INTEGER,
        created_on INTEGER
        last_modified_on INTEGER
        )
        '''
    crsr.execute(qry_create_entries)

def init_DB():
    dbfile = getPath(4)

    #connect to database
    connection = sql3.connect(dbfile)

    #cursor
    crsr = connection.cursor()

    print(getString("db_connected_EN"))



    connection.close()
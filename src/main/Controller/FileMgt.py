import os

'''
----------------------------------------------------
[LogNo] [Date]      [Name]  [Description]
----------------------------------------------------
001     18-04-22    FKL     Create file
                            Add function:
                                - getPath
                                - getColumnId
002     10-04-2022  FKL     Function getPath
                                - add db path as option 4
003     23-04-2022  FKL     Function getColumnId
                                - add login

This module delivers all information regarding the entries file 
'''

def getPath(pathType: int) -> str:
    '''
        1 -> fileName
        2 -> directory path
        3 -> file path
        4 -> db path
    '''
    path = os.environ['HOMEPATH'] + '\\SPArGEl'  # get home path
    fileName = 'entries.csv'
    dbname = 'entries.db'
    if pathType == 4:
        return path+"\\"+dbname
    elif pathType == 3:
        return path+"\\"+fileName
    elif pathType == 2:
        return path
    elif pathType == 1:
        return fileName
    else:
        raise Exception("type provided must be 1, 2, 3, 4 - input: " +str(pathType))


def getColumnId(columnName: str) -> int:
    columnName = columnName.lower()
    if columnName == "id":
        return 0
    elif columnName == "name":
        return 1
    elif columnName == "login":
        return 2
    elif columnName == "description":
        return 3
    elif columnName == "cipher":
        return 4
    elif columnName == "shift":
        return 5
    elif columnName == "created_on":
        return 6
    elif columnName == "last_modified_on":
        return 7
    else:
        return -1 # invalid column name
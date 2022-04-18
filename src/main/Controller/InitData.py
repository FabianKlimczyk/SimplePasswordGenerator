'''
---------------------------------------------------
[LogNo] [Date]      [Name]  [Description]
----------------------------------------------------
001     10-04-22    FKL     Create file
                            Add functions:
                                - directoryExists
                                - createNewDirectory
                                - fileExists
                                - createNewFile
002     15-04-22    FKL     Add function:
                                - getPath
'''


import os
import src.main.Controller.WriteData as wd
from src.main.Controller.FileMgt import getPath

def directoryExists(path: str) -> bool:
    # prepare dir creation in not existent
    if not os.path.isdir(path):
        return createNewDirectory(path)
    else:
        return True


def createNewDirectory(path: str) -> bool:
    # create dir if no existent
    os.mkdir(path)
    if os.path.isdir(path):
        print("The directory path {} was created".format(path))
        return True
    else:
        return False


def fileExists(filePath: str) -> bool:
    # prepare file creation in not existent
    if not os.path.isfile(filePath):
        return createNewFile(filePath)
    else:
        return True


def createNewFile(filePath: str) -> bool:
    #create pw file if not existent
    try:
        if wd.writeInitalData():
            print("The directory path {} was created".format(filePath))
            return True
    except FileExistsError:
        pass #writeLog
    else:
        return False


def loadData() -> bool:
    # starting point of the class
    if directoryExists(getPath(2)):
        if fileExists(getPath(3)):
            print("The data and files are ready!")
            return True
        else:
            print("Something went wrong. Please check your file manually!")
    else:
        print("Something went wrong. Please check your directory manually!")
    # file or dir is not ready
    return False

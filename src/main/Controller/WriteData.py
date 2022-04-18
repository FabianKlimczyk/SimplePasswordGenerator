'''
----------------------------------------------------
[LogNo] [Date]      [Name]  [Description]
----------------------------------------------------
001     10-04-22    FKL     Create file
                            Add functions:
                                - directoryExists
                                - createNewDirectory
                                - fileExists
                                - createNewFile
                                - write
                                - writeData
002     16-04-22    FKL     Add functions:
                                - writeNewData
                                - deleteData
                                - updateData
                            Delete functions:
                                - writeData
                                - write
003     18-04-22    FKL     Add functions:
                                - writeUpdateByPos
                                - writeUpdateByName
                            Delete functions:
                                - updateData
'''

import csv
import src.main.Model.Entry as Entry
from src.main.Controller.FileMgt import getPath, getColumnId


def writeInitalData() -> bool:
    filePath = getPath(3)
    with open(filePath, 'w', newline='') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow(['id', 'name', 'description', 'cipher', 'shift', 'created_on', 'last_modified_on'])
    return True


def writeUpdateByPos(pos: int, columnName: str, updateText: str) -> bool:
    columnIdx = getColumnId(columnName)
    if columnIdx > 0 and columnIdx < 4:
        filePath = getPath(3)
        found = False
        with open(filePath, 'r') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            rowIdNo = 0
            lines = []
            for line in reader:
                lines.append(line)
                if rowIdNo == pos:
                    # TODO 1) in case of password, must be different from old one
                    lines[pos][columnIdx] = updateText
                    found = True
                rowIdNo += 1
        if found:
            with open(filePath, 'w', newline='') as csvfile:
                filewriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                filewriter.writerows(lines)
            return True
        else:
            return False
    else:
        # only name, description and cipher can be changed
        return False


def writeUpdateByName(name: str, updateText: str) -> bool:
    columId = getColumnId("name")
    #TODO update line of passed name
    pass


def writeNewData(entry: Entry.Entry) -> bool:
    filePath = getPath(3)
    with open(filePath, 'a', newline='') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        #TODO 1) check if name already exists
        entrylst = [getattr(entry, field) for field in entry.__dataclass_fields__]
        filewriter.writerow(entrylst)
    return True


def deleteData(id: int):
    #TODO delete row with id == id
    pass

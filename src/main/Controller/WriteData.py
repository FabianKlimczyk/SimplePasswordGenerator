import csv
import src.main.Database.Entry as Entry
from src.main.Controller.InitData import getPath


def writeInitalData() -> bool:
    filePath = getPath(3)
    with open(filePath, 'w', newline='') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow(['id', 'name', 'description', 'cipher', 'shift', 'created_on', 'last_modified_on'])
    return True


def writeUpdate(field: str, text: str):
    #TODO 1) in case of password, must be different frim old one
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
    pass

import csv


def writeInitalData(filePath: str) -> bool:
    with open(filePath, 'w') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow(['id', 'name', 'description', 'password', 'created_on', 'last_modified_on'])
    return True

def write():
    pass

def writeData():
    pass

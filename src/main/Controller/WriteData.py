import os

def directoryExists(path: str) -> bool:
    if not os.path.isdir(path):
        return createNewDirectory(path)
    else:
        return True

def createNewDirectory(path: str) -> bool:
    os.mkdir(path)
    if os.path.isdir(path):
        print("The directory path {} was created".format(path))
        return True
    else:
        return False

def fileExists(filePath: str) -> bool:
    if not os.path.isfile(filePath):
        return createNewFile(filePath)
    else:
        return True

def createNewFile(filePath: str) -> bool:
    try:
        open(filePath,'x')
        print("The directory path {} was created".format(filePath))
        return True
    except FileExistsError:
        pass #writeLog
    else:
        return False

def write():
    pass

def writeData():
    path = os.environ['HOMEPATH']+'\\SPArGEl'
    fileName = 'entries.txt'
    if directoryExists(path):
        if fileExists(path+'\\'+fileName):
            pass #open file
        else:
            print("Something went wrong. Please check your file manually!")
    else:
        print("Something went wrong. Please check your directory manually!")


writeData()

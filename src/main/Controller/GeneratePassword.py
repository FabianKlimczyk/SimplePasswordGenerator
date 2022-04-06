import random as rnd

def getPassword(charList,numberOfChars=int) -> str:
    password = ""
    for i in range (numberOfChars):
        index = rnd.randint(0,len(charList)-1)
        password = password + rnd.choice(charList[index])
    return password

def createCharList(charList, inclUpperCase=bool, inclNumbers=bool, inclSpecialChars=bool):
    charList.append(list('abcdefghijklmnopqrstuvwyxz'))
    if inclUpperCase:
        charList.append(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if inclNumbers:
        charList.append(list('0123456789'))
    if inclSpecialChars:
        charList.append(list('.,;-_!?$%&()+#'))
    return charList

def generatePassword(length=int, inclUpperCase=bool,inclNumbers=bool,inclSpecialChars=bool) -> str:
    charList = []
    charList = createCharList(charList,inclUpperCase,inclNumbers,inclSpecialChars)
    return getPassword(charList,length)

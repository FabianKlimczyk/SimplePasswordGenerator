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
        charList.append(list('.;-_!?$%&()+#'))
    return charList


def generatePassword(length=int, inclUpperCase=bool,inclNumbers=bool,inclSpecialChars=bool) -> str:
    """
    Entry point of the module

    :param length: length of the password
    :param inclUpperCase: include upper case characters
    :param inclNumbers: include number characters
    :param inclSpecialChars: include special characters
    :return: return as password
    """
    charList = []
    charList = createCharList(charList,inclUpperCase,inclNumbers,inclSpecialChars)
    return getPassword(charList,length)

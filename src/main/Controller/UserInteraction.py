from src.main.Controller.ReadData import getNumberOfLines
from src.main.Controller.GeneratePassword import generatePassword as gnrt_pw
from src.main.Controller.DeEnCoding import encode as encode
from src.main.Controller.WriteData import writeNewData
import src.main.Database.Entry as Entry
import time
import random

def createEntry() -> Entry.Entry:
    """
    creates an db entry based on the user input
    :return: Entry
    """

    # user input
    name = input("Please enter a name!: ")
    descr = input("Please enter a description!: ")
    pwLength = int(input("Please enter the password length!: "))
    inclUpperCase = input("Do you want to include upper case letters? y/n ").lower() == "y"
    inclNumbers = input("Do you want to include numbers? y/n ").lower() == "y"
    inclSpecialCharacters = input("Do you want to include special letters? y/n ").lower() == "y"

    id = getNumberOfLines()+1
    shift = random.randint(1,76)
    # encode created password
    enc_pw = encode(
            gnrt_pw(pwLength,inclUpperCase,inclNumbers,inclSpecialCharacters),shift
        )
    return Entry.Entry(id,name,descr,enc_pw,shift,time.time(),time.time())


def userLoop()-> None:
    while action := input("What do you want to do? (c)ontinue or (q)uit? Please insert c or q").lower() != "q":
        inp = input("Do you want to (c)reate a new entry or (l)oad an existent one? c/l ").lower()

        if inp == "c":
            print("Crating a new entry...")
            entry = createEntry()
            writeNewData(entry)
            print("The entry {} was created".format(entry.name))

        elif inp == "l":
            # load and show existent entry
            print("load")
            pass
        else:
            print("{} is not a valid input! c/l !!!".format(inp))
    print("Program quit!")
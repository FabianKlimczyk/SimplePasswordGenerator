'''
---------------------------------------------------
[LogNo] [Date]      [Name]  [Description]
----------------------------------------------------
001     11-04-22    FKL     Create file
                            Add functions:
                            - createEntry
                            - userLoop
002     15-04-22    FKL     function:
                                - createEntry - get necessary information for creation
003     18-04-22    FKL     add function:
                                - updateEntry

'''

from src.main.Controller.ReadData import getNumberOfLines
from src.main.Controller.GeneratePassword import generatePassword as gnrt_pw
from src.main.Controller.DeEnCoding import encode as encode
from src.main.Controller.WriteData import writeNewData, writeUpdateByPos
import src.main.Model.Entry as Entry
import src.main.Database.DBMgt as db
import sqlite3 as sql3
import time
import random



def createEntry() -> Entry.Entry:
    """
    creates an db entry based on the user input
    :return: Entry
    """

    # user input
    name = input("Please enter a name!: ")
    login = input("Please enter your login")
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
    return Entry.Entry(id,name,login,descr,enc_pw,shift,time.time(),time.time())


def updateEntry() -> bool:
    #TODO Funktion überflüssig
    id = int(input("In which row do you want to change a field? Please enter the id: ").lower())
    name = input("Which field do you want to chagne? ").lower()
    update = input("What is your new updatedText? ")
    return writeUpdateByPos(id,name,update)


def userLoop(conn: sql3.Connection) -> None:
    while action := input("What do you want to do? (c)ontinue or (q)uit? Please insert c or q").lower() != "q":
        inp = input("Do you want to (c)reate, (l)oad, (u)pdate, (d)elete? ").lower()

        if inp == "c":
            print("Creating a new entry...")
            entry = createEntry()
            db.insertEntry(conn, entry)
            print("The entry {} was created".format(entry.name))
        elif inp == "l":
            # load and show existent entry
            print("Loading...")
            #TODO abfrgae ob bestimmter record angezeigt werden soll
            data = db.getEntry(conn, "","")
            for i in data:
                print(i)
        elif inp == "u":
            print("Updating...")
            name = input("Which record do you want to change? Please enter the name!: ")
            column = input("Which column do you want to change?: ") + "= ?"
            newValue = input("Please enter a new value: ")
            if db.updateEntry(conn, name,column,newValue):
                print("The entry was updated")
            else:
                print("Update is not possible. Please try again")
        elif inp == "d":
            print("Deleting...")
            id = input("Which id do you want to delete? ")
            if db.deleteEntryById(conn, id):
                print("The entry was deleted")
            else:
                print("Deletion is not possible! Please try again.")
        else:
            print("{} is not a valid input! c/l/u/d !!!".format(inp))
    print("Program quit!")
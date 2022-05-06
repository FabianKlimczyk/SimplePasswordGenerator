'''
---------------------------------------------------
[LogNo] [Date]      [Name]  [Description]
----------------------------------------------------
001     11-04-22    FKL     Create file
                            Add functions:
                            - createEntry
                            - userLoop
002     15-04-22    FKL     function createEntry
                                - get necessary information for creation
003     18-04-22    FKL     add function:
                                - updateEntry
004     06-05-22    FKL     function createEntry
                                - entry id always 0 because of autoincrement
                            function userLoop
                                - implement filter for loading data

'''

from src.main.Controller.GeneratePassword import generatePassword as gnrt_pw
from src.main.Controller.DeEnCoding import encode as encode
import src.main.Model.Entry as Entry
import src.main.Database.DBMgt as db
import src.main.Database.DataMgt as datamgt
from src.main.Utility.Strings import getString
import sqlite3 as sql3
import time
import random



def createEntry() -> Entry.Entry:
    """
    creates an db entry based on the user input
    :return: Entry
    """

    # user input
    name = input(getString("inp_name","EN")+"\n").strip()
    login = input(getString("inp_login","EN")+"\n").strip()
    descr = input(getString("inp_descr","EN")+"\n").strip()
    pwLength = int(input(getString("inp_pw_length","EN")+"\n").strip())
    inclUpperCase = input(getString("inp_incl_upper_case","EN")+"\n").lower().strip() == "y"
    inclNumbers = input(getString("inp_incl_numb","EN")+"\n").lower().strip() == "y"
    inclSpecialCharacters = input(getString("inp_incl_spec_char","EN")+"\n").lower().strip() == "y"

    shift = random.randint(1,76)
    # encode created password
    enc_pw = encode(
            gnrt_pw(pwLength,inclUpperCase,inclNumbers,inclSpecialCharacters),shift
        )
    return Entry.Entry(0,name,login,descr,enc_pw,shift,time.time(),time.time())

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
            showAll = input("Do you want to see all entries? y/n\n").lower()
            if showAll == "y":
                datamgt.showData(conn, '','')
            else:
                getPw = input("Get password? y/n\n").lower()
                column = input("Which colum do you want to filter?\n")
                filterValue = input("Please enter the filter value\n")
                if getPw == "y":
                    datamgt.getPassword(conn,column,filterValue)
                else:
                    datamgt.showData(conn, column, filterValue)
        elif inp == "u":
            print("Updating...")
            name = input("Which record do you want to change? Please enter the name!: ")
            column = f" last_modified_on = {time.time()}, "+input("Which column do you want to change?: ") + "= ?"
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
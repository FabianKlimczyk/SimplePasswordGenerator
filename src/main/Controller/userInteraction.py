import src.main.Database.Entry as Entry
import time

def createEntry() -> Entry.Entry:
    name = input("Please enter a name! ")
    descr = input("Please enter a description! ")

    return Entry.Entry("",name,descr,"pw",time.time(),time.time())

def userLoop()-> None:
    while action := input("What do you want to do? (c)ontinue or (q)uit? Please insert c or q").lower() != "q":
        inp = input("Do you want to create a new entry or load an existent one? c/l ").lower()

        if inp == "c":
            print("Crating a new entry...")
            entry = createEntry()
            print(entry)

        elif inp == "l":
            # load and show existent entry
            print("load")
            pass
        else:
            print("{} is not a valid input! c/l !!!".format(inp))
    print("Program quit!")

userLoop()
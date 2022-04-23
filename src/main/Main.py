'''---------------------------------------------------
[LogNo] [Date]      [Name]  [Description]
----------------------------------------------------
001     11-04-22    FKL     Create file
                            Add functions:
                            - main
'''


import Controller.InitData as loadData
import Controller.UserInteraction as uia
import Database.DBMgt as db

def main() -> None:
    # Entry point of the application
    #loadData.loadData()
    #print("The database is ready!")
    db.init_DB()
    uia.userLoop()


if __name__ == '__main__':
    main()

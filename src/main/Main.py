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
    connection = db.getDatabaseConnection()
    uia.userLoop(connection)


if __name__ == '__main__':
    main()

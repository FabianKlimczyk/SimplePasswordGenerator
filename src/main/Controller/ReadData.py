'''
----------------------------------------------------
[LogNo] [Date]      [Name]  [Description]
----------------------------------------------------
001     15-04-22    FKL     Create file
                            Add function:
                                - getNumberOfLines
002     16-04-22    FKL     Update function:
                                - getNumberOfLines -> fix output
003     18-04-22    FKL     Update function:
                                - getNumberOfLines -> fix calculation
'''

import src.main.Controller.InitData as initData
import csv


def getNumberOfLines() -> int:
    """

    :return: total number of data rows
    """
    file = initData.getPath(3)
    noOfLines = 0
    with open(file, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for _ in reader:
            noOfLines += 1
    return noOfLines


def getUserInfo(name: str) -> str:
    #TODO return the row of the corresponding user name
    pass
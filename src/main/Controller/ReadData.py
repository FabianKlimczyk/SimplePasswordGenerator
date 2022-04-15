import src.main.Controller.InitData as initData
import pandas as pd


def getNumberOfLines() -> int:
    """

    :return: total number of data rows
    """
    file = initData.getPath(3)
    data = pd.read_csv(file)
    return len(data)-1


def getUserInfo(name: str) -> str:
    #TODO return the row of the corresponding user name
    pass
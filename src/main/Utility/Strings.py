# English strings
db_connected_EN = "Connected to database"

# German strings
db_connected_DE = "Verbindung zur Datenbank wurde hergestellt!"


def getString(stringName: str) -> str:
     # return the string of the corresponding stringName
     return globals().get(stringName)
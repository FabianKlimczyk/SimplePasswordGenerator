'''
----------------------------------------------------
[LogNo]   [Date]         [Name]    [Description]
----------------------------------------------------
001       19-04-2022     FKL       Created
                                   Add functions:
                                        - getString

File to store and get all strings for every available language
!!! Please always add each of the following languages
- English, German
'''

# English strings
db_connected_EN = "Connected to database"

# German strings
db_connected_DE = "Verbindung zur Datenbank wurde hergestellt!"


def getString(countryCode: str, stringName: str) -> str:
     # return the string of the corresponding stringName
     return globals().get(stringName+"_"+countryCode)
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
db_created_EN = "Database created"
db_ready_EN = "Database is ready"

# German strings
db_connected_DE = "Verbindung zur Datenbank wurde hergestellt!"
db_created_DE = "Datenbank erstellt"
db_ready_DE = "Datenbank ist bereit"

def getString(stringName: str, countryCode: str) -> str:
     # return the string of the corresponding stringName
     return globals().get(stringName+"_"+countryCode.upper())
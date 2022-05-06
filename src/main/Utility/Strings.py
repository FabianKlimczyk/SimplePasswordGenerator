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
# Database
db_connected_EN = "Connected to database"
db_created_EN = "Database created"
db_ready_EN = "Database is ready"

# Inputs
inp_name_EN = "Please enter the entry name: "
inp_login_EN = "Please enter the login: "
inp_descr_EN = "Please enter a description: "
inp_pw_length_EN = "Please enter the password length: "
inp_incl_upper_case_EN = "Do you want to include upper case letters? y/n"
inp_incl_numb_EN = "Do you want to include numbers? y/n"
inp_incl_spec_char_EN = "Do you want to include special letters? y/n"

# German strings
#Database
db_connected_DE = "Verbindung zur Datenbank wurde hergestellt!"
db_created_DE = "Datenbank erstellt"
db_ready_DE = "Datenbank ist bereit"

# Inputs

def getString(stringName: str, countryCode: str) -> str:
     # return the string of the corresponding stringName
     return globals().get(stringName+"_"+countryCode.upper())
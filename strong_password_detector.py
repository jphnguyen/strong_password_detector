# !python3
# strong_password_detector.py - Will make sure password is eight characters long with at least ONE lowercase,
# ONE uppercase and ONE numerical value.
import re
print("Password needs to be at least 8-15 characters long with at least one uppercase, one lower case,\nand one numerical value to be secure")
def detector():
    while True:
        password = input("Please enter password you wish to use here: ")
        character_regex = re.compile(r"\w{8,15}$")
        lowercase_regex = re.compile(r"[a-z]")
        uppercase_regex = re.compile(r"[A-Z]")
        number_regex    = re.compile(r"[0-9]")

        if character_regex.search(password) == None:
            print("Password needs to be at least 8-15 characters long.")
            continue
        elif lowercase_regex.search(password) == None:
            print("Password needs at least one lowercase character.")
            continue
        elif uppercase_regex.search(password) == None:
            print("Password needs at least one uppercase character.")
            continue
        elif number_regex.search(password) == None:
            print("Password needs at least one numerical value.")
            continue
        else:
            print("Password is very secure.")
            break

detector()
# !python3
# strong_password_detector.py - Will make sure password is eight characters long with at least ONE lowercase,
# ONE uppercase and ONE numerical value.
import re

print("Password needs to be at least 8-15 characters long with at least one uppercase, one lower case,\nand one numerical value to be secure")

def detector():
    while True:
        password = input("Please enter password you wish to use here: ")

        password_regex = re.compile(r"""
        (?=.*[a-z])    # at least one lowercase character
        (?=.*[A-Z])    # at least one uppercase character
        (?=.*[0-9])    # at least one digit
        .{8,}          # at least eight characters long  
        """, re.VERBOSE)

        if password_regex.search(password) == None:
            print("""Needs to be:\n
            eight characters long,\n
            at least one lowercase character,\n
            at least one uppercase character,\n
            and at least one number.
            """)
            continue
        else:
            print("Password is very secure.")
            break

detector()
# The final project is the same points as the other assignments for the class.
# It combines elements of the homeworks and recompiles them into a new project.
# The goal of this project is to create a password verification tool that ensures compliance with password complexity requirements.

# Project Requirements:
# Take input of a password and use that password to compare against the following complexity requirements:
# Password must be 8 characters or more
# Password may not contain your name or the words pass, word, or password
# Must contain a capital letter
# Must contain a symbol
# Must contain a number
# Once password is verified as defined as valid, build in a hash function and then build a function to decode the hash.
# The hash functions can be found all over the internet.  Just look up Password Hash Function Python.
# When finished, submit your link to the github code.

import re, hashlib

password= input("Enter a password:")
while True:
    if (len(password)<8):
        break
    elif re.search("Connor", password, re.IGNORECASE):
        print("*Invalid password*")
        print("Password cannot contain: your name")
        break
    elif re.search("House", password, re.IGNORECASE):
        print("*Invalid password*")
        print("Password cannot contain: your name")
        break
    elif re.search("pass", password, re.IGNORECASE):
        print("*Invalid password*")
        print("Password cannot contain: pass")
        break
    elif re.search("word", password, re.IGNORECASE):
        print("*Invalid password*")
        print("Password cannot contain: word")
        break
    elif re.search("password", password, re.IGNORECASE):
        print("*Invalid password*")
        print("Password cannot contain: password")
        break
    elif not re.search("[A-Z]", password):
        print("*Invalid password*")
        print("The password must contain one capital letter at minimum.")
        break
    elif not re.search("[0-9]", password):
        print("*Invalid password*")
        print("The password must contain one number at minimum.")
        break
    elif not re.search("[a-z + 0-9 + A-Z]",password):
        break
    elif not re.search("[!@#$%^&*()-=_+`~,.<>;|?]",password):
        break
    elif re.search("\s",password):
        break
    else:
        flag = 0
        print("Status: ")
        print("Valid Password")
        print(" ")
        print("Password Hash: ")
        hash0 = hashlib.md5(password.encode()).hexdigest()
        print(hash0)
        chkPass = input("To confirm your password re-enter it: ")
        password == hashlib.md5(chkPass.encode()).hexdigest()
        if (password == chkPass):
            print("*Successful Decoding*")
        else:
            print("*Unsuccessful Decoding*")
        break

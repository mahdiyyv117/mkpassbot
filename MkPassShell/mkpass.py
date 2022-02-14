import string
import random

# all possible scenarios for string
character = string.ascii_letters + string.digits + string.punctuation
password = ""

try:
    # number of password characters
    numch = int(input("number of characters "))
    if numch < 8:
        # for a good password
        print("please enter a larger number")
    else:
        # choice a random password
        for i in range(numch):
            password += random.choice(character)
        print("your password", password, sep="\n")
except ValueError:
    print("please enter the correct value")

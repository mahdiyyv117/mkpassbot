import string
import random

numch = int(input("number of characters "))
character = string.ascii_letters + string.digits + string.punctuation
password = ""

if numch < 8:
    print("please enter a larger number")
else:
    for i in range(numch):
        password += random.choice(character)
    print("your password", password, sep="\n")

import pickle
import os
import csv
import re
try:
    from colorama import Fore, Style, init
    init(autoreset=True)
except ImportError:
    pass

# -------- Definitions --------

class dataClass(object):
    def __init__(self):
        self.data = []

    def enter(self, inputLine="> ", isFieldName=False):
        if not isFieldName:
            inp = trans(input(inputLine))
            self.data.append(inp)
        else:
            inp = input(inputLine)
            if inp.isidentifier():
                self.data.append(inp)
        return inp

def typeOf(dataStr):
    """ Returns type of the data passed."""
    for a in dataStr:
        if not (a.isdigit() or a == "." or a == "-"):
            return "str"
    if dataStr.count(".") <= 1:
        return "num"

def trans(string):
    """ Transforms string to number."""
    for a in string:
        if not (a.isdigit() or a == "." or a == "-"):
            return string
    return eval(string)


def main():
    while True:
        print("""
Make a selection: 

1) Add a record
2) Delete a record
3) Edit a record
4) Overwrite the file
5) Display as table
6) Display as csv
7) Plot a Graph (BETA)
8) Find in table
9) Import CSV
10) Export As...
11) Switch DB
12) EXIT
""")
        choice = input("Enter your choice: ")
        if choice == "12":
            print("Exiting kunalDB.")
            break
        else:
            print("Feature not implemented yet.")

if __name__ == "__main__":
    main()
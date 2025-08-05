import pickle
import os
import csv
import re
try:
    from colorama import Fore, Style, init
    init(autoreset=True)
except ImportError:
    pass

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
# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Ryan Ciupak
# Date: Sept 30, 2026
# Purpose: Practice adding and removing elements in list.
# Usage: ./lab3d.py

# Follow the specific instructions given in the README.md file

myList = [1, 2, 3, 4, 5, 6]
print(myList)
myList.append(7)
print(myList)
myList.insert(0,0)
print(myList)
myList.remove(1)
print(myList)

for i in myList:
    if i == myList.index(6):
        print(f"The index of value 6 is: {i}")

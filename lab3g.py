# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Ryan Ciupak
# Date: Sept. 30, 2026
# Purpose: 
# Usage: ./lab3g.py

# Follow the specific instructions given in the README.md file

myList = []

n = int(input("Select a number: "))

while len(myList) < 6:
    myList.append(n)
    n = n * 10
myList.sort(reverse=True)
print(myList)
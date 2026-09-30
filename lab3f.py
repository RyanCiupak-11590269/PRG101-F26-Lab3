# Add comments before you do anything else.

#!/usr/bin/env python3
# Author:
# Date:
# Purpose: 
# Usage: ./lab3f.py

# Follow the specific instructions given in the README.md file

matrix = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
]

element = matrix[1][1]
print(element)
element = matrix[0][1]
print(element)
element = matrix[2][2]
print(element)
for i in range(3):
    for j in range(3):
     print(matrix[i][j])
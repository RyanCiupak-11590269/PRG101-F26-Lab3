# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Ryan Ciupak
# Date: Sept. 30, 2026
# Purpose: 
# Usage: ./lab3a.py

import random
numbers = []

for i in range(20):
    numbers.append(random.randint(0, 99))
print(numbers)
numbers.sort()
print(numbers)
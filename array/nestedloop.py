# Quest: 1.	Generate 14 random numbers (1<number<10),
#           store them in an array, output all the values of this array.
#           Check if there are values are repetitive.
#           Output "there are repetitive values"
#                   or "there is no repetitive value" after the check.
#
# For this and nestedloop2.py,
#   14 integers chosen in range 2-9 must have repetitive values,
#   so we generate floats which have one decimal place.

import random

numbers: list = random.choices([x / 10 for x in range(11, 100)], k=14)
print("There are repetitive values"
      if len(set(numbers)) != len(numbers)
      else "There is no repetitive value")

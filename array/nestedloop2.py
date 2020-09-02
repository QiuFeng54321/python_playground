# Quest: 2.	Generate 14 random numbers (1<number<10),
#           store them in an array,
#           output all the values of this array.
#           Check if there are values are repetitive.
#           Output "there are repetitive values"
#                   or "there is no repetitive value" after the check,
#           stop the program immediately
#               when you found there are repetitive values in the array.

import random

numbers: list = random.choices([x / 10 for x in range(11, 100)], k=14)
print(numbers)

freq_dict: dict = {}

for i in numbers:
    if i not in freq_dict.keys():
        freq_dict[i] = 0
    freq_dict[i] += 1
    if freq_dict[i] > 1:
        print("There are repetitive values")
        exit()
print("There is no repetitive value")

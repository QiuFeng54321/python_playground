# Quest: 3.	Generate 14 random numbers (1<number<10),
#           store them in an array,
#           output all the values of this array.
#           Output the index of first repetitive values in the array.

import random

numbers: list = random.choices(list(range(2, 10)), k=14)
print(numbers)

freq_dict: dict = {}

for i in range(len(numbers)):
    element: int = numbers[i]
    if element not in freq_dict.keys():
        freq_dict[element] = 0
    freq_dict[element] += 1
    if freq_dict[element] > 1:
        print(f"There are repetitive values at index {i}")
        exit()
print("There is no repetitive value")

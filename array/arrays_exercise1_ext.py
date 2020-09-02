# Quest: 1.	Given an array of integers [2, 8, 9, 4, 5],
#           output the maximum and minimum.
#           Swap the maximum and minimum in this array,
#           then output the new array.

import random

numbers: list = random.choices(list(range(2, 10)), k=5)
maximum, minimum = numbers.index(max(numbers)), numbers.index(min(numbers))
print(f"Maximum: {numbers[maximum]}, Minimum: {numbers[minimum]}")

numbers[maximum], numbers[minimum] = numbers[minimum], numbers[maximum]
print(f"Swapped array: {numbers}")
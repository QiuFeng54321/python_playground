# Quest: 1.	Create an array of length n
#               containing random numbers (1<number<10),
#               output the second-maximum element.

import random

numbers: list = random.choices(list(range(2, 10)), k=5)
print(numbers)

maximum, second_maximum = 0, 0

for i in numbers:
    # M2 < i < M1
    if second_maximum < i and i < maximum:
        second_maximum = i
    # M1 < i
    elif maximum < i:
        second_maximum = maximum
    maximum = max(maximum, i)

print(f"Maximum: {maximum}, Second Maximum: {second_maximum}")

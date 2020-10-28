# 1028-2

import random

magic_number: int = random.randint(0, 100)
try_count: int = 0

while int(input("Guess: ")) != magic_number:
    print("Tay again!")
    try_count += 1

print("You got it!")
print("Number of times tried:", try_count + 1)  # Include correct try

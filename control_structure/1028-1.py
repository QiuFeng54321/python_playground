# 1028-1

import random

magic_number: int = random.randint(0, 100)

while int(input("Guess: ")) != magic_number:
    print("Tay again!")

print("You got it!")

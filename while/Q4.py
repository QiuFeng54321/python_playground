# Quest: 4. Input 5 numbers, output the number of odd and even number

i: int = 0
evens: int = 0
odds: int = 0
while i < 5:
    num: int = int(input(f"Number {i + 1}: "))
    if num % 2 == 0:
        evens += 1
    else:
        odds += 1
    i += 1
print(f"There are {evens} even numbers and {odds} odd numbers")

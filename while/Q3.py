# Quest: 3.	Input 5 numbers, output the odd and even numbers

i: int = 0
odds: list = []
evens: list = []
while i < 5:
    num: float = float(input(f"Number {i + 1}: "))
    if num % 2 == 0:
        evens.append(str(num))
    else:
        odds.append(str(num))
    i += 1

print(f"Odds: {', '.join(odds)}")
print(f"Evens: {', '.join(evens)}")

# Quest: 1.	Input 5 numbers, output the total and average of these number.

i: int = 0
total: float = 0
while i < 5:
    total += float(input(f"Number {i + 1}: "))
    i += 1
print("Total:", total)
print("Average:", total / 5.0)

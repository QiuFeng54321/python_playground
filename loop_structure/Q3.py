# Quest: 3.	Input 1000 numbers, output the total and average of these number

input_amount: int = 1000
total: float = 0
average: float = 0

for i in range(input_amount):
    num: float = float(input(f"Number {i + 1}: "))
    total += num
    average += num / input_amount

print(f"Total: {total}")
print(f"Average: {average}")

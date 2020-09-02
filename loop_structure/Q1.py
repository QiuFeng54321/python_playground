# Quest: 1.	Input three number, output the largest number and smallest number.
# *Loop structure required*

# Task brief info
print("Input three numbers: x, y, z.")

# Loop structure in list comprehension
numbers = [float(input(f"{chr(120 + i)}: ")) for i in range(3)]

# Just use max and min func
print(f"The largest number is {max(numbers)}.")
print(f"The smallest number is {min(numbers)}.")

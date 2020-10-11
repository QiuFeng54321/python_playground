# Quest: 5.	Input 5 numbers,
#           output the number of positive numbers and
#                  negative number you have input

i: int = 0
positives: int = 0
negatives: int = 0

while i < 5:
    num: float = float(input(f"Number {i + 1}: "))
    if num >= 0:
        positives += 1
    else:
        negatives += 1
    i += 1
print(f"There are {positives} positive numbers and "
      f"{negatives} negative numbers")

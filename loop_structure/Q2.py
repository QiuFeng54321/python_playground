# Quest: 2.	Keep Input numbers, stop input when you input -1,
# output the number of positive numbers and negative number

positives, negatives = 0, 0

while (num := float(input("Input a number [any/-1(quit)]: "))) != -1:
    if num >= 0:
        positives += 1
    else:
        negatives += 1

print(
    f"There are {positives} positive numbers and {negatives} negative numbers."
)

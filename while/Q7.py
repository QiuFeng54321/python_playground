# Quest: 7.	Keep Input numbers,
#           stop input when you input -1,
#           output the number of
#           positive numbers and negative number you have input
#           (you can’t count -1 into the negative number)

positives: int = 0
negatives: int = 0

while (num := int(input("Num: "))) != -1:
    if num >= 0:
        positives += 1
    else:
        negatives += 1

print(f"There are {positives} positive numbers and"
      f"{negatives} negative numbers")

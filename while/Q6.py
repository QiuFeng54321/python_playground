# Quest: 6.	Input Number and n, Write algorithm to output the Number ** n

num: float = float(input("Number: "))
n: int = int(input("Exponent: "))
res: float = 1
for i in range(n):
    res *= num
print("Result:", res)

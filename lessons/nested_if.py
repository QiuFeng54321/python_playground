import global_func
# Q1

global_func.inc()

mark: float = float(input("Student Mark: "))
print("The grade is", "A" if mark >= 80 else "B" if mark >= 70 else
      "C" if mark >= 60 else "U")

# Q2

global_func.inc()

print([
    "num1 " + comp + " num2"
    for num1, num2 in [global_func.inp_generic(2, float)]
    for comp in [">" if num1 > num2 else "<" if num1 < num2 else "is equal to"]
][0])

# Q3

global_func.inc()

print([
    res
    for inp in [float(input("A number plssssssss: "))]
    for res in [
        "is in range" if inp in range(11) else
        "is too large" if inp > 10 else
        "is too small"
    ]
][0])

# Q4

global_func.inc()

print("Quadrant", [
    quadrant
    for x, y in [global_func.inp(2)]
    for quadrant in [
        1 if x > 0 and y > 0 else
        2 if x < 0 and y > 0 else
        3 if x < 0 and y < 0 else
        4 if x > 0 and y < 0 else
        None
    ]
][0])

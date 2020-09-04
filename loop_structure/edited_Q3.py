# Quest: 3. Input two integers x and y,
#           print their sum,
#           but if it is more than 100 or less than 0,
#           print "out of range"

print(
    [
        f"Sum: {sum}\n{'out of range' if sum not in range(101) else ''}"
        for sum in [int(input("x: ")) + int(input("y: "))]
    ][0]
)

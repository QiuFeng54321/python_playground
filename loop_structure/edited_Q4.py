# Quest: 4. Input two integers x and y,
#           print x - y,
#           if it is less than or equal to 10,
#               print 'x - y is less than or equal to 10'

print([
    f"x - y = {diff}" + (f"\n{'x - y <= 10'}" if diff <= 10 else "")
    for diff in [int(input("x: ")) - int(input("y: "))]
][0])

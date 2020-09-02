from global_func import inc, inp


# 1
inc()
print(x := int(input("x: ")) + (y := int(input("y: "))))

# 2
inc()
print(max(x := int(input("x: ")), y := int(input("y: "))))

# 3
inc()
print([
    x * (x % 2) + y * (y % 2) + z * (z % 2)
    for x, y, z in [inp(3)]
][0])

# 4
inc()
print([
    sum if sum in range(101) else "out of range"
    for sum in [int(input("x: ")) + int(input("y: "))]
][0])

# 5
inc()
print([
    f"{max(x, y, z)}, {min(x, y, z)}"
    for x, y, z in [inp(3)]
][0])

# 6
inc()
print([
    f"{xs}{ys}{zs}"
    for x, y, z in [inp(3)]
    for xs in [f"{x} = {y} + {z}\n" if x == y + z else ""]
    for ys in [f"{y} = {x} + {z}\n" if y == x + z else ""]
    for zs in [f"{z} = {y} + {x}\n" if z == y + x else ""]
][0])

# 7
inc()
print([
    res
    for x, y, z in [inp(3)]
    for res in ["all same" if x == y and y == z else
                "x = y" if x == y else
                "y = z" if y == z else
                "x = z" if x == z else "all distinct"]
][0])

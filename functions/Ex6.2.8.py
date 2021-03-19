def _calc_area(side_length=10):
    return side_length ** 2


def calculate_area(side_length=10):
    if side_length <= 0:
        return _calc_area()
    return _calc_area(side_length)


print(
    f"The area of a square with sides of length {(side_length := int(input('Enter side length: ')))} is {calculate_area(side_length)}.")

# Gaddis 5.5 Property Tax

def computePropertyTax(value: float) -> None:
    print(f"Assessment value: {value * 0.6}")
    print(f"Property Tax: {value * 0.6 * 0.0072}")


value: float = float(input("Actual value of a piece of property: "))
computePropertyTax(value)

# Gaddis 5.8 Paint Job Estimator


def calculate_paint_volume(area: float) -> float:
    return area / 112


def calculate_labor_hours(volume: float) -> float:
    return volume * 8


def calculate_paint_cost(volume: float, price: float) -> float:
    return volume * price


def calculate_labor_cost(labor_hours: float) -> float:
    return labor_hours * 35


def total_cost(area: float, price: float) -> float:
    volume = calculate_paint_volume(area)
    return calculate_labor_cost(calculate_labor_hours(volume)) + calculate_paint_cost(volume, price)

area: float = float(input("Square feet of the wall space to be painted: "))
price: float = float(input("Price of the paint per gallon: "))
print(f"Total cost: {total_cost(area, price)}")

# Gaddis 5.12 Maximum of Two Values

# Why not just do max??????????? There is LITERALLY a built-in one!!!
def max(a, b):
    if a > b:
        return a
    return b
a, b = int(input("A: ")), int(input("B: "))
print(f"Max: {max(a, b)}")

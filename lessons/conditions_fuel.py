coefficients: tuple = (.176, .236, .208, .296)
fuel_type: int = 2 if input("Fuel type: ") == "petrol" else 0
volume: int = 1 if float(input("Input the volume: ")) > 2 else 0
distance: float = float(input("Distance: "))
print("Emmision is", coefficients[fuel_type + volume] * distance / 1000)

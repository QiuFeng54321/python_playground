# Lalalalalalala I don't use condition statement yeahhhhhhhhhhhhhhhhhhhh
coefficients: tuple = (.176, .236, .208, .296)
fuel_type: int = int(input("Fuel type: ") == "petrol") * 2
volume: int = int(float(input("Input the volume: ")) > 2)
distance: float = float(input("Distance: "))
print("Emmision is", coefficients[fuel_type + volume] * distance / 1000)

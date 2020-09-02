# Quest: 10.	Extension task2:
#               Write algorithm to output the (1!+2!+3!+…………….number!)
#               Number should be input by keyboard.

import math

print("Sigma i! for i in 1..n:",
      sum(
          [
              math.factorial(n + 1)
              for n in range(int(input("Factorial number upper bound: ")))
          ]
      ))

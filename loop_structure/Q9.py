# Quest: 9.	Extension task1:
#           Write algorithm to output the result of (1!+2!+3!+…………….100!)

import math

print("Sigma n! for n in 1..100:",
      sum([math.factorial(n + 1) for n in range(100)]))

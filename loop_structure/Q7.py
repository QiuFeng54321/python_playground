# Quest: 7.	Write algorithm to output the result of (1²+ 2²+ 3²+…………….Number²),
#           Number should be input by keyboard

print("Sum of all f(x) = x^2 for x be 0..n:",
      sum([(n + 1)**2 for n in range(int(input("Number upper bound: ")))])
      )

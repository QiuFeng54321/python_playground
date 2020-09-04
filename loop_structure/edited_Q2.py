# Quest: 2. Input integer x,
#           if it is an odd number,
#           output 'it is an odd number',
#           if it is an even number,
#           output 'it is an even number'.

print(
    [
        f"it is an {'odd' if x % 2 == 1 else 'even'} number"
        for x in [int(input("Input a number: "))]
    ][0]
)

# Quest 4.	Write an algorithm, using FOR loop structure
#               to input 500 numbers into an array.
#               Write an algorithm, using a single loop,
#               to print the 500 numbers you have stored in array.
#               Rewrite your algorithm using another loop structure.

# From global_func
def inp(num: int) -> list:
    return [int(input(f"{i + 1}: ")) for i in range(num)]


def print_array(array: list) -> None:
    for i in array:
        print(i)


def print_array_2(array: list) -> None:
    i = 0
    while i < len(array):
        print(array[i])
        i += 1


print_array(inp(500))

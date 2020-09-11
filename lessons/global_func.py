def inp(num: int) -> list:
    return [int(input(f"{chr(120 + i)}: ")) for i in range(num)]


def inp_generic(num, cls: type) -> list:
    return [cls(input(f"{chr(120 + i)}: ")) for i in range(num)]


acc = 0


def inc():
    global acc
    acc += 1
    print('-' * 40)
    print(f"Current question: {acc}")
    print('-' * 40)


def product(*args):
    res = 1.0
    for i in args:
        res *= i
    return res

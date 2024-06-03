def recursion_exponent_n_m(n: int, m: int) -> int:
    if m == 0:
        result = 1
    elif m < 0:
        result = 1 / recursion_exponent_n_m(n, -m)
    else:
        result = n * recursion_exponent_n_m(n, m - 1)

    return result


print(recursion_exponent_n_m(3, 3))

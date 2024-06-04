def recursion_exponent_n_m(n: int, m: int, result=1) -> int:
    if m == 0:
        return result
    elif m < 0:
        return 1 / recursion_exponent_n_m(n, -m, result=result)
    else:
        return recursion_exponent_n_m(n, m - 1, result * n)


print(recursion_exponent_n_m(3, 0))
print(recursion_exponent_n_m(3, -2))
print(recursion_exponent_n_m(3, 4))

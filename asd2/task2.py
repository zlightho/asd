def recursion_sum_of_digits(number: int) -> int:
    if number == 0:
        result = 0
    else:
        last_digit = number % 10
        remaining = number // 10
        result = last_digit + recursion_sum_of_digits(remaining)
    return result


print(recursion_sum_of_digits(10001))

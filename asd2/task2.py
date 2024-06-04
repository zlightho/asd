def recursion_sum_of_digits(number: int, sum_of_digits=0) -> int:
    if number == 0:
        return sum_of_digits
    else:
        last_digit = number % 10
        remaining = number // 10
        return recursion_sum_of_digits(remaining, sum_of_digits + last_digit)


print(recursion_sum_of_digits(10201))

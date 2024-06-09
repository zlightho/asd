def recursion_is_palindrom(string: str) -> bool:
    left = 0
    right = len(string) - 1

    if left >= right:
        return True
    if string[left] != string[right]:
        return False
    return recursion_is_palindrom(string[left + 1:right])
def recursion_is_palindrom(string: str) -> bool:
    if len(string) <= 1:
        return True
    if string[0] != string[-1]:
        return False
    return recursion_is_palindrom(string[1:-1])
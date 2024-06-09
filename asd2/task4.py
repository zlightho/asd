def is_palindrom(string: str) -> bool:
    def recursion_is_palindrom(string: str, left: int, right: int) -> bool:
        if left >= right:
            return True
        if string[left] != string[right]:
            return False
        return recursion_is_palindrom(string, left + 1, right - 1)
    return recursion_is_palindrom(string, 0, len(string) - 1)

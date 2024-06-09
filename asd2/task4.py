def recursion_is_palindrom(string: str, left: int, right: int) -> bool:
        if left >= right:
            return True
        if string[left] != string[right]:
            return False
        return recursion_is_palindrom(string, left + 1, right - 1)
    
def is_palindrom(string: str) -> bool:
    return recursion_is_palindrom(string, 0, len(string) - 1)
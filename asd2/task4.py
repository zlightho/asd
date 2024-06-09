def recursion_is_palindrom(string: str, left=None, right=None) -> bool:
    if left is None:
        left = 0
    if right is None:
        right = len(string) - 1

    if left >= right:
        return True
    if string[left] != string[right]:
        return False
    return recursion_is_palindrom(string, left + 1, right - 1)
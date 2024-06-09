def recursion_is_palindrom(string: str, left=None, right=None) -> bool:
    if left is None:
        left = 0
    if right is None:
        right = len(string) - 1

    if left >= right:
        return True
    # Если символы на текущих указателях не равны, строка не палиндром
    if string[left] != string[right]:
        return False
    # Рекурсивный вызов с продвижением указателей
    return recursion_is_palindrom(string,left + 1, right - 1)

my_string="арозаупаланалапуазора"
recursion_is_palindrom(my_string)

from typing import List


def recursive_find_second_max(spisok: List, max1, max2, index):
    if index >= len(spisok):
        return max2

    current_value = spisok[index]

    if current_value > max1:
        max2 = max1
        max1 = current_value
    elif current_value == max1:
        max2 = max1
    elif current_value > max2:
        max2 = current_value

    return recursive_find_second_max(spisok, max1, max2, index + 1)


def find_second_max(spisok: List):
    if spisok[0] > spisok[1]:
        max1, max2 = spisok[0], spisok[1]
    elif spisok[0] <= spisok[1]:
        max1, max2 = spisok[1], spisok[0]
    return recursive_find_second_max(spisok, max1, max2, 2)


my_list = (1, 2, 4, 5, 6, 6)
print(find_second_max(my_list))

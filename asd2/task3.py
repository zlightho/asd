from typing import List


def recursion_list_length(spisok: List[int], length=0) -> int:
    if not spisok:
        return 0
    spisok.pop(0)
    return 1 + recursion_list_length(spisok)


my_list = [1, 2]
print(recursion_list_length(my_list))

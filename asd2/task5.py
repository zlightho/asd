from typing import List

def recursive_print_even_values(spisok: List[int]) -> None:
    if not spisok:
        return
    value = spisok.pop(0)
    if value % 2 == 0:
        print(value)
    recursive_print_even_values(spisok)

def print_even_values(spisok: List[int]) -> None:
    recursive_print_even_values(spisok)

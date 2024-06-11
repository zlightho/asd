from typing import List

def recursive_print_even_values(spisok: List[int], index: int) -> None:
    if index >= len(spisok):
        return
    if spisok[index] % 2 == 0:
        print(spisok[index])
    recursive_print_even_values(spisok, index + 1)

def print_even_values(spisok: List[int]) -> None:
    recursive_print_even_values(spisok, 0)

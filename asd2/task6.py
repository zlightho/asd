from typing import List

def recursive_print_even_indexes(spisok: List[int], index: int) -> None:
    if index >= len(spisok):
        return
    if index % 2 == 1:
        print(spisok[index])
    recursive_print_even_indexes(spisok, index + 1)

def print_even_indexes(spisok: List[int]) -> None:
    recursive_print_even_indexes(spisok,0)
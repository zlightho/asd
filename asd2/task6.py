from typing import List

def recursive_print_even_indexes(spisok: List[int], index: int) -> None:
    if index >= len(spisok):
        return
    print(spisok[index])
    recursive_print_even_indexes(spisok, index + 2)

def print_even_indexes(spisok: List[int]) -> None:
    recursive_print_even_indexes(spisok,1)

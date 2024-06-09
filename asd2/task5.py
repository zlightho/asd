from typing import List
def recursive_print_even_values(spisok: List) -> None:
    if not spisok:
        return
    if spisok[0] % 2 == 0:
        print(spisok[0])
    recursive_print_even_values(spisok[1:])
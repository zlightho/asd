from typing import List
def recursive_print_even_indexes(spisok: List, index: int = 0) -> None:
    if index >= len(spisok):
        return
    if index % 2 == 1:
        print(spisok[index])
    recursive_print_even_indexes(spisok,index+1)
    

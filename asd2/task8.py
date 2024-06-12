import os
from typing import List


def recursive_find_files(directory: str) -> List[str]:
    files_list = []
    for entry in os.listdir(directory):
        full_path = os.path.join(directory, entry)
        if os.path.isdir(full_path):
            recursive_find_files(full_path)
        else:
            files_list.append(full_path)
    return files_list


def find_all_files(directory: str) -> List[str]:
    return recursive_find_files(directory)

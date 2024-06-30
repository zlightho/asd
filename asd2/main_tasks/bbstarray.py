def GenerateBBSTArray(a):
    # Сортируем входной массив
    a = sorted(a)

    # Начальная длина дерева
    tree_size = 2 ** (len(a).bit_length()) - 1
    array_bst = [None] * tree_size

    _binary_sort(a, array_bst, 0)
    return array_bst


def _binary_sort(a, tree, index):
    if not a:
        return
    # Центрированный элемент текущего массива
    mid = len(a) // 2
    # Помещаем центрированный элемент в дерево
    tree[index] = a[mid]

    # Рекурсивно заполняем левую и правую часть дерева
    _binary_sort(a[:mid], tree, 2 * index + 1)
    _binary_sort(a[mid + 1 :], tree, 2 * index + 2)

def GenerateBBSTArray(a):
    a = sorted(a)

    tree_size = 2 ** (len(a).bit_length()) - 1
    array_bst = [None] * tree_size

    _binary_sort(a, array_bst, 0)
    return array_bst


def _binary_sort(a, tree, index):
    if not a:
        return None
    mid = len(a) // 2
    tree[index] = a[mid]
    _binary_sort(a[:mid], tree, 2 * index + 1)
    _binary_sort(a[mid + 1 :], tree, 2 * index + 2)

class BSTNode:

    def __init__(self, key, val, parent):
        self.NodeKey = key
        self.NodeValue = val
        self.Parent = parent
        self.LeftChild = None
        self.RightChild = None
        self.Level = 0


class BSTFind:

    def __init__(self):
        self.Node = None

        self.NodeHasKey = False
        self.ToLeft = False


class BST:

    def __init__(self, node):
        self.Root = node

    def FindNodeByKey(self, key):
        result = BSTFind()
        current = self.Root

        while current is not None:
            if current.NodeKey == key:
                result.Node = current
                result.NodeHasKey = True
                return result
            elif key < current.NodeKey:
                if current.LeftChild is None:
                    result.Node = current
                    result.ToLeft = True
                    return result
                current = current.LeftChild
            else:
                if current.RightChild is None:
                    result.Node = current
                    return result
                current = current.RightChild

        return result

    def AddKeyValue(self, key, val):
        find_result = self.FindNodeByKey(key)

        if find_result.NodeHasKey:
            return False

        new_node = BSTNode(key, val, find_result.Node)

        if find_result.Node is None:
            self.Root = new_node
        else:
            if find_result.ToLeft:
                find_result.Node.LeftChild = new_node
            else:
                find_result.Node.RightChild = new_node

        return True

    def FinMinMax(self, FromNode, FindMax):
        current = FromNode
        if FindMax:
            while current.RightChild is not None:
                current = current.RightChild
        else:
            while current.LeftChild is not None:
                current = current.LeftChild
        return current

    def DeleteNodeByKey(self, key):
        find_result = self.FindNodeByKey(key)

        if not find_result.NodeHasKey:
            return False

        node_to_delete = find_result.Node

        if node_to_delete.LeftChild is None and node_to_delete.RightChild is None:
            if node_to_delete == self.Root:
                self.Root = None
            else:
                if node_to_delete.Parent.LeftChild == node_to_delete:
                    node_to_delete.Parent.LeftChild = None
                else:
                    node_to_delete.Parent.RightChild = None

        elif node_to_delete.LeftChild is None or node_to_delete.RightChild is None:
            if node_to_delete.LeftChild is not None:
                child = node_to_delete.LeftChild
            else:
                child = node_to_delete.RightChild

            if node_to_delete == self.Root:
                self.Root = child
            else:
                if node_to_delete.Parent.LeftChild == node_to_delete:
                    node_to_delete.Parent.LeftChild = child
                else:
                    node_to_delete.Parent.RightChild = child
            child.Parent = node_to_delete.Parent

        else:
            successor = self.FinMinMax(node_to_delete.RightChild, False)
            node_to_delete.NodeKey = successor.NodeKey
            node_to_delete.NodeValue = successor.NodeValue
            if successor.Parent.LeftChild == successor:
                successor.Parent.LeftChild = successor.RightChild
            else:
                successor.Parent.RightChild = successor.RightChild
            if successor.RightChild is not None:
                successor.RightChild.Parent = successor.Parent

        return True

    def Count(self):
        return self._CountRecursive(self.Root)

    def _CountRecursive(self, node):
        if node is None:
            return 0
        return (
            1
            + self._CountRecursive(node.LeftChild)
            + self._CountRecursive(node.RightChild)
        )

    def WideAllNodes(self):
        if self.Root is None:
            return []

        queue = [self.Root]
        result = []

        while queue:
            node = queue.pop(0)
            result.append(node)
            if node.LeftChild is not None:
                queue.append(node.LeftChild)
            if node.RightChild is not None:
                queue.append(node.RightChild)

        return result

    def DeepAllNodes(self, order):
        result = []

        def in_order(node):
            if node is not None:
                in_order(node.LeftChild)
                result.append(node)
                in_order(node.RightChild)

        def post_order(node):
            if node is not None:
                post_order(node.LeftChild)
                post_order(node.RightChild)
                result.append(node)

        def pre_order(node):
            if node is not None:
                result.append(node)
                pre_order(node.LeftChild)
                pre_order(node.RightChild)

        if order == 0:
            in_order(self.Root)
        elif order == 1:
            post_order(self.Root)
        elif order == 2:
            pre_order(self.Root)

        return result


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


class BalancedBST:
    def __init__(self):
        self.Root = None

    def GenerateTree(self, a):
        if not a:
            self.Root = None
        a.sort()
        self.Root = self._generate_tree(a, 0, len(a) - 1, None, 0)
        return self.Root

    def _generate_tree(self, a, start, end, parent, level):
        if start > end:
            return None
        mid = (start + end) // 2
        node = BSTNode(a[mid], None, parent)
        node.Level = level
        node.LeftChild = self._generate_tree(a, start, mid - 1, node, level + 1)
        node.RightChild = self._generate_tree(a, mid + 1, end, node, level + 1)
        return node

    def IsBalanced(self, root_node):
        if root_node is None:
            return True

        def check_balance(node):
            if node is None:
                return 0, True
            left_height, left_balanced = check_balance(node.LeftChild)
            right_height, right_balanced = check_balance(node.RightChild)
            current_balanced = abs(left_height - right_height) <= 1
            current_height = max(left_height, right_height) + 1
            return current_height, left_balanced and right_balanced and current_balanced

        _, is_balanced = check_balance(root_node)
        return is_balanced

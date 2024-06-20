class BSTNode:

    def __init__(self, key, val, parent):
        self.NodeKey = key
        self.NodeValue = val
        self.Parent = parent
        self.LeftChild = None
        self.RightChild = None


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

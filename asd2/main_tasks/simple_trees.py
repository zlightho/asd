class SimpleTreeNode:

    def __init__(self, val, parent):
        self.NodeValue = val  # значение в узле
        self.Parent = parent  # родитель или None для корня
        self.Children = []  # список дочерних узлов


class SimpleTree:

    def __init__(self, root):
        self.Root = root  # корень, может быть None

    def AddChild(self, ParentNode, NewChild):
        # ваш код добавления нового дочернего узла существующему ParentNode
        if ParentNode is not None:
            ParentNode.Children.append(NewChild)
            NewChild.Parent = ParentNode

    def DeleteNode(self, NodeToDelete):
        # ваш код удаления существующего узла NodeToDelete
        if NodeToDelete.Parent is not None:
            NodeToDelete.Parent.Children.remove(NodeToDelete)
            NodeToDelete.Parent = None
        nodes_to_delete = NodeToDelete.Children[:]
        for child in nodes_to_delete:
            self.DeleteNode(child)

    def GetAllNodes(self):
        # ваш код выдачи всех узлов дерева в определённом порядке
        if self.Root is None:
            return []
        result = []
        self._GetAllNodesRecursive(self.Root, result)
        return result

    def _GetAllNodesRecursive(self, node, result):
        result.append(node)
        for child in node.Children:
            self._GetAllNodesRecursive(child, result)

    def FindNodesByValue(self, val):
        # ваш код поиска узлов по значению
        result = []
        if self.Root is not None:
            self._FindAllNodesRecursive(self.Root, val, result)
        return result

    def _FindAllNodesRecursive(self, node, val, result):
        if node.NodeValue == val:
            result.append(node)
        for child in node.Children:
            self._FindAllNodesRecursive(child, val, result)

    def MoveNode(self, OriginalNode, NewParent):
        # ваш код перемещения узла вместе с его поддеревом --
        # в качестве дочернего для узла NewParent
        if OriginalNode is not None and NewParent is not None:
            OriginalNode.Parent.Children.remove(OriginalNode)
            NewParent.Children.append(OriginalNode)
            OriginalNode.Parent = NewParent

    def Count(self):
        # количество всех узлов в дереве
        return len(self.GetAllNodes())

    def LeafCount(self):
        # количество листьев в дереве
        all_nodes = self.GetAllNodes()
        return sum(1 for node in all_nodes if not node.Children)

    def SetLevels(self):
        if self.Root is None:
            return
        self._SetLevelsRecursive(self.Root, 0)

    def _SetLevelsRecursive(self, node, level):
        node.Level = level
        for child in node.Children:
            self._SetLevelsRecursive(child, level + 1)

    
    def EvenTrees(self):
        if self.Root is None:
            return []

        to_remove = []
        self._check_even_subtree(self.Root, to_remove)
        return [(to_remove[i], to_remove[i + 1]) for i in range(0, len(to_remove), 2)]

    def _count_nodes(self, node):
        if node is None:
            return 0
        count = 1
        for child in node.Children:
            count += self._count_nodes(child)
        return count

    def _check_even_subtree(self, node, to_remove):
        for child in node.Children:
            self._check_even_subtree(child, to_remove)
            if self._count_nodes(child) % 2 == 0:
                to_remove.append(node)
                to_remove.append(child)

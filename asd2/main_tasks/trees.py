    class SimpleTreeNode:
        
        def __init__(self, val, parent):
            self.NodeValue = val # значение в узле
            self.Parent = parent # родитель или None для корня
            self.Children = [] # список дочерних узлов
        
    class SimpleTree:

        def __init__(self, root):
            self.Root = root # корень, может быть None
        
        def AddChild(self, ParentNode, NewChild):
            if ParentNode is not None:
                ParentNode.Children.append(NewChild)
                NewChild.Parent = ParentNode
    
        def DeleteNode(self, NodeToDelete):
            if NodeToDelete.Parent is not None:
                NodeToDelete.Parent.Children.remove(NodeToDelete)
                NodeToDelete.Parent = None
            nodes_to_delete = NodeToDelete.Children[:]
            for child in nodes_to_delete:
                self.DeleteNode(child)

        def GetAllNodes(self):
            if self.Root is None:
                return None
            result = []
            return self._GetAllNodesRecursive(self, result)
        
        def _GetAllNodesRecursive(self, result):
            result.append(self)
            for child in self.Children:
                self._GetAllNodesRecursive(child, result)
            

        def FindNodesByValue(self, val):
            
    
        def MoveNode(self, OriginalNode, NewParent):
            # ваш код перемещения узла вместе с его поддеревом -- 
            # в качестве дочернего для узла NewParent
            pass  
    
        def Count(self):
            # количество всех узлов в дереве
            return 0

        def LeafCount(self):
            # количество листьев в дереве
            return 0

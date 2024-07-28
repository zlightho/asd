class Stack:
    def __init__(self):
        self.stack = []

    def size(self):
        return len(self.stack)

    def pop(self):
        if len(self.stack) != 0:
            return self.stack.pop()
        else:
            return None

    def push(self, value):
        self.stack.append(value)

    def peek(self):
        if len(self.stack) != 0:
            return self.stack[-1]
        else:
            return None

    def __iter__(self):
        return iter(self.stack)


class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.items.pop(0)

    def size(self):
        return len(self.items)

    def is_empty(self):
        return len(self.items) == 0


class Vertex:
    def __init__(self, val):
        self.Value = val
        self.Hit = False


class SimpleGraph:
    def __init__(self, size):
        self.max_vertex = size
        self.m_adjacency = [[0] * size for _ in range(size)]
        self.vertex = [None] * size

    def AddVertex(self, v):
        for i in range(self.max_vertex):
            if self.vertex[i] is None:
                self.vertex[i] = Vertex(v)
                return

    def RemoveVertex(self, v):
        if v < 0 or v >= self.max_vertex or self.vertex[v] is None:
            return
        self.vertex[v] = None
        for i in range(self.max_vertex):
            self.m_adjacency[v][i] = 0
            self.m_adjacency[i][v] = 0

    def IsEdge(self, v1, v2):
        if v1 < 0 or v1 >= self.max_vertex or v2 < 0 or v2 >= self.max_vertex:
            return False
        return self.m_adjacency[v1][v2] == 1

    def AddEdge(self, v1, v2):
        if v1 < 0 or v1 >= self.max_vertex or v2 < 0 or v2 >= self.max_vertex:
            raise Exception("AddEdge error.")
        self.m_adjacency[v1][v2] = 1
        self.m_adjacency[v2][v1] = 1

    def RemoveEdge(self, v1, v2):
        if v1 < 0 or v1 >= self.max_vertex or v2 < 0 or v2 >= self.max_vertex:
            raise Exception("RemoveEdge error.")
        self.m_adjacency[v1][v2] = 0
        self.m_adjacency[v2][v1] = 0

    def DepthFirstSearch(self, VFrom, VTo):

        if VFrom < 0 or VFrom >= self.max_vertex or VTo < 0 or VTo >= self.max_vertex:
            return []
        if self.vertex[VFrom] is None or self.vertex[VTo] is None:
            return []

        # 0) Очищаем все дополнительные структуры данных: делаем стек пустым,
        # а все вершины графа отмечаем как непосещённые
        for v in self.vertex:
            if v is not None:
                v.Hit = False

        path = Stack()
        # 1) Выбираем текущую вершину X. Для начала работы это будет исходная вершина А.
        if self._dfs(VFrom, VTo, path):
            return [self.vertex[v] for v in path]

        return []

    def _dfs(self, current, VTo, path):
        # 2) Фиксируем вершину X как посещённую.
        self.vertex[current].Hit = True

        # 3) Помещаем вершину X в стек.
        path.push(current)

        # 4) Ищем среди смежных вершин вершины X целевую вершину Б.
        if current == VTo:
            # Если она найдена, записываем её в стек и возвращаем сам стек как результат работы (путь из А в Б).
            return True

        for i in range(self.max_vertex):
            # Если целевой вершины среди смежных нету, то выбираем среди смежных такую вершину, которая ещё не была посещена.
            if self.m_adjacency[current][i] == 1 and not self.vertex[i].Hit:
                # Если такая вершина найдена, делаем её текущей X и переходим к п. 2.
                if self._dfs(i, VTo, path):
                    return True

        # 5) Если непосещённых смежных вершин более нету, удаляем из стека верхний элемент.
        path.pop()
        # Если стек пуст, то прекращаем работу и информируем, что путь не найден.
        # В противном случае делаем текущей вершиной X верхний элемент стека, помечаем его как посещённый, и после чего переходим к п. 4.
        return False

    def BreadthFirstSearch(self, VFrom, VTo):
        if VFrom < 0 or VFrom >= self.max_vertex or VTo < 0 or VTo >= self.max_vertex:
            return []
        if self.vertex[VFrom] is None or self.vertex[VTo] is None:
            return []

        # Если начальная и конечная вершины совпадают, возвращаем эту вершину.
        if VFrom == VTo:
            return [self.vertex[VFrom]]

        # Помечаем все вершины как непосещённые
        for v in self.vertex:
            if v is not None:
                v.Hit = False

        queue = Queue()
        queue.enqueue(VFrom)  # Шаг 1: Начинаем с исходной вершины
        self.vertex[VFrom].Hit = True  # Помечаем её как посещённую

        # Инициализация словаря предшественников, чтобы отслеживать путь
        prev = {VFrom: None}

        while not queue.is_empty():
            current = queue.dequeue()

            # Шаг 2: Проверяем все смежные вершины текущей вершины
            for i in range(self.max_vertex):
                if self.m_adjacency[current][i] == 1 and not self.vertex[i].Hit:
                    # Шаг 3: Помечаем найденную смежную вершину как посещённую
                    self.vertex[i].Hit = True
                    prev[i] = current
                    queue.enqueue(i)

                    # Если нашли целевую вершину, формируем путь и возвращаем его
                    if i == VTo:
                        path = []
                        while i is not None:
                            path.append(i)
                            i = prev[i]
                        return [self.vertex[v] for v in reversed(path)]

        return []

    def WeakVertices(self):
        weak_vertices = []
        for v in range(self.max_vertex):
            if self.vertex[v] is None:
                continue
            neighbors = [
                i for i in range(self.max_vertex) if self.m_adjacency[v][i] == 1
            ]
            found_triangle = False
            for i in range(len(neighbors)):
                for j in range(i + 1, len(neighbors)):
                    if self.m_adjacency[neighbors[i]][neighbors[j]] == 1:
                        found_triangle = True
                        break
                if found_triangle:
                    break
            if not found_triangle:
                weak_vertices.append(self.vertex[v])
        return weak_vertices

    def isConnected(self, i, j, k):
        return (
            self.m_adjacency[i][j] == 1
            or self.m_adjacency[j][k] == 1
            or self.m_adjacency[k][i] == 1
        )


def print_weak_vertices(graph):
    weak_vertices = graph.WeakVertices()
    print("Weak vertices:", [v.Value for v in weak_vertices])


# Создаем граф
graph = SimpleGraph(5)
graph.AddVertex(1)
graph.AddVertex(2)
graph.AddVertex(3)
graph.AddVertex(4)
graph.AddVertex(5)

# Добавляем ребра
graph.AddEdge(0, 1)
graph.AddEdge(1, 2)
graph.AddEdge(2, 0)  # Треугольник 0-1-2

graph.AddEdge(3, 4)  # Отдельное ребро

# Проверка слабых вершин
print_weak_vertices(graph)  # Ожидаемый результат: вершины 3 и 4

graph.AddEdge(0, 3)
graph.AddEdge(1, 3)
graph.AddEdge(2, 4)

print_weak_vertices(graph)  # Ожидаемый результат: вершина 4

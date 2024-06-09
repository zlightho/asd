class Deque:
    '''7.1.Мера сложности для операций addHead/removeHead и addTail/removeTail
    будет различаться из-за разных способов доступа к элементам внутренней
    структуры данных (в данном случае стандартного списка).

    Операции addHead/removeHead работают с началом списка,
    и если внутренний список реализован как динамический массив,
    то добавление и удаление элемента из начала списка может потребовать
    сдвига всех последующих элементов. В этом случае мера сложности будет O(n),
    где n - размер очереди.
    Операции addTail/removeTail работают с концом списка и,
    если внутренний список реализован как динамический массив,
    добавление и удаление элемента из конца списка выполняются эффективно за время O(1).'''
    def __init__(self):
        self.deque = []

    def addFront(self, item):
        self.deque.insert(0, item)

    def addTail(self, item):
        self.deque.append(item)

    def removeFront(self):
        if len(self.deque) > 0:
            return self.deque.pop(0)
        else:
            return None

    def removeTail(self):
        if len(self.deque) > 0:
            return self.deque.pop()
        else:
            return None

    def size(self):
        return len(self.deque)

def recursion_is_palindrom(string):
    char_deque = Deque()

    for char in string:
        char_deque.addTail(char)

    def check_palindrome(deq):
        if deq.size() <= 1:
            return True
        front = deq.removeFront()
        tail = deq.removeTail()
        if front != tail:
            return False
        return check_palindrome(deq)

    return check_palindrome(char_deque)
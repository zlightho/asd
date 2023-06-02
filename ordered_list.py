class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None


class OrderedList:
    def __init__(self, asc):
        self.head = None
        self.tail = None
        self.__ascending = asc

    def compare(self, v1, v2):
        if v1 < v2:
            return -1
        elif v1 > v2:
            return 1
        else:
            return 0

    def add(self, value):
        node = Node(value)

        if self.head is None:
            self.head = node
            self.tail = node
            return

        current = self.head

        if (self.__ascending and self.compare(node.value, current.value) <= 0) or \
                (not self.__ascending and self.compare(node.value, current.value) >= 0):
            node.next = current
            current.prev = node
            self.head = node
            return

        while current.next is not None:
            if (self.__ascending and self.compare(node.value, current.value) > 0 and self.compare(node.value, current.next.value) <= 0) or \
                    (not self.__ascending and self.compare(node.value, current.value) < 0 and self.compare(node.value, current.next.value) >= 0):
                node.prev = current
                node.next = current.next
                current.next.prev = node
                current.next = node
                return

            current = current.next

        current.next = node
        node.prev = current
        self.tail = node

    def find(self, val):
        current = self.head

        while current is not None:
            if self.compare(current.value, val) == 0:
                return current
            elif (self.__ascending and self.compare(current.value, val) > 0) or \
                    (not self.__ascending and self.compare(current.value, val) < 0):
                return None
            current = current.next

        return None

    def delete(self, val):
        current = self.head

        while current is not None:
            if self.compare(current.value, val) == 0:
                if current.prev is not None:
                    current.prev.next = current.next
                else:
                    self.head = current.next

                if current.next is not None:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev

                return
            elif (self.__ascending and self.compare(current.value, val) > 0) or \
                    (not self.__ascending and self.compare(current.value, val) < 0):
                return
            current = current.next

    def clean(self, asc):
        self.__ascending = asc
        self.head = None
        self.tail = None

    def len(self):
        count = 0
        current = self.head

        while current is not None:
            count += 1
            current = current.next

        return count

    def get_all(self):
        r = []
        current = self.head

        while current is not None:
            r.append(current.value)
            current = current.next

        return r


class OrderedStringList(OrderedList):
    def __init__(self, asc):
        super(OrderedStringList, self).__init__(asc)

    def compare(self, v1, v2):
        v1_stripped = v1.strip()
        v2_stripped = v2.strip()

        if v1_stripped < v2_stripped:
            return -1
        elif v1_stripped > v2_stripped:
            return 1
        else:
            return 0

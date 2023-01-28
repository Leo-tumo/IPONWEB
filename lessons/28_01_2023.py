log = print


class Queue:
    def __init__(self):
        self.array = []

    def push(self, value):
        self.array.append(value)

    def pop(self):
        return self.array.remove(self.array[0])

    def front(self):
        return self.array[0]

    def back(self):
        return self.array[len(self.array) - 1]

    def size(self):
        return len(self.array)

    def empty(self):
        return not self.size()


class Stack:
    def __init__(self):
        self.c = []
        self.size = 0

    def top(self):
        return self.c[self.size - 1]

    def empty(self):
        return not self.size

    def size(self):
        return self.size

    def push(self, value):
        self.c.append(value)
        self.size += 1

    def pop(self):
        if self.size:
            self.size -= 1
            return self.c.pop()
        else:
            raise IndexError

    def __eq__(self, other):
        return self.c == other.c

    def __iter__(self):
        raise StopIteration

    def __next__(self):
        pass

    def __getitem__(self, value):
        raise IndexError


class Node:
    def __init__(self, previous: 'Node', nxt: 'Node' = None, data=None):
        self.prev = previous
        self.next = nxt
        self.data = data

    @property
    def prev(self):
        return self._prev

    @prev.setter
    def prev(self, value):
        self._prev = value

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, value):
        self._next = value

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_node(self, node):
        if self.head is None:
            self.head = node
            node.prev = None
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        self.tail = node.next

    def search(self, value):
        temp = self.head
        while temp is not None:
            if temp.data == value:
                return temp
            temp = temp.next

    def delete_at_head(self):
        dl = self.head
        self.head = self.head.next
        del dl

    def delete_at_tail(self):
        self.tail = self.tail.prev
        del self.tail.next
        self.tail.next = None

    def insert_at_tail(self, node):
        temp: Node.data = node
        temp.next = None
        if self.head is None:
            self.head = temp
            temp.head = None
        else:
            temp.prev = self.tail.prev
            self.tail = self.tail.next
            temp.next = self.tail








if __name__ == '__main__':
    st = Stack()
    for i in range(30):
        st.push(i)
    log(st.pop())

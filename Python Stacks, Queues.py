from collections import deque
class Queue:
    def __init__(self):
        self._elements = deque()

    def __len__(self):
        return len(self._elements)

    def __iter__(self):
        while len(self) > 0:
            yield self.deqeue()

    def enqueue(self, elemetn):
        self._elements.append(element)

    def dequeue(self):
        return self._elements.popleft()

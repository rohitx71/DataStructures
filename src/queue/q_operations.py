"""
Implement Queue using arrays from scratch python
https://runestone.academy/runestone/books/published/pythonds/BasicDS/ImplementingaStackinPython.html
"""
import ctypes


class Queue:
    def __init__(self, capacity=5):
        self.arr = self.make_array(capacity)
        self.front = -1
        self.rear = -1
        self.capacity = capacity
        self.count = 0

    def enqueue(self, val):
        if self.rear == self.capacity-1:
            return OverflowError("Queue overflow")
        if self.front == -1 and self.rear == -1:
            self.front = self.rear = 0
        else:
            self.rear = self.rear + 1
        self.arr[self.rear] = val
        self.count += 1

    def deque(self):
        if self.front == -1 or self.front > self.rear:
            return IndexError("Queue underflow")
        self.arr[self.front] = None
        self.front = self.front + 1 % self.capacity
        self.count -= 1

    def print_elements(self):
        i = self.front
        while i <= self.rear:
            print(self.arr[i])
            i += 1

    def peek(self):
        return self.arr[self.rear]

    def make_array(self, new_cap):
        try:
            return (new_cap * ctypes.py_object)()
        except Exception as e:
            print(e)


if __name__ == "__main__":
    q = Queue()
    q.enqueue(5)
    q.enqueue(6)
    q.enqueue(7)
    print(q.peek())
    q.print_elements()
    q.enqueue(8)
    q.deque()
    q.print_elements()



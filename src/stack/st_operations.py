"""
Implement Stack using python
https://runestone.academy/runestone/books/published/pythonds/BasicDS/ImplementingaStackinPython.html
"""
import ctypes


class Stack:
    def __init__(self, size=5):
        self.A = []
        self.len = len

    def push(self, ele):
        if len(self.A) == self.len:
            return IndexError("Overflow")
        self.A.append(ele)

    def pop(self):
        if len(self.A) == 0:
            return IndexError("Underflow")
        self.A.pop()

    def peek(self):
        if len(self.A) == 0:
            return -1
        return self.A[len(self.A)-1].data


class Node:
    def __init__(self, val):
        self.data = val


if __name__ == "__main__":
    s=Stack()
    s.push(Node(5))
    s.push(Node(6))
    s.push(Node(9))
    print(s.peek())
    s.pop()
    print(s.peek())
    s.pop()
    print(s.peek())
    s.pop()
    print(s.peek())
    print(s.peek())

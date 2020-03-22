"""
https://www.geeksforgeeks.org/implementation-of-dynamic-array-in-python/
Creates python list from scratch
"""
import ctypes

class DynamicArray:
    def __init__(self):
        self.n = 0  # actual elements
        self.capacity = 4  # length
        self.A = self.make_array(self.capacity)

    def make_array(self, new_cap):
        return (new_cap * ctypes.py_object)()

    def __len__(self):
        return self.n

    def append(self, val):
        if self.n == self.capacity:
            self._resize(self.capacity * 2)
        self.A[self.n] = val
        self.n += 1

    def __get_item__(self, i):
        if not 0 < i < self.n:
            return IndexError("Array out of bounds")
        return self.A[i]

    def _resize(self, new_cap):
        B = self.make_array(self.n * 2)
        for i in range(self.n):
            B[i] = self.__get_item__(i)
        self.capacity = new_cap
        self.A = B


if __name__ == "__main__":
    arr = DynamicArray()
    arr.append(4)
    arr.append(3)
    print(arr.__len__())
    print(arr)

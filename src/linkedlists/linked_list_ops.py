class Node:
    def __init__(self, data):
        self.next = None
        self.data = data


class LinkedList:
    def __init__(self):
        self.head = None

    def truncate(self):
        self.head = None

    def traverse(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next

    def insert_at_start(self, value):
        tmp = Node(value)
        tmp.next = self.head
        self.head = tmp

    def append(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = Node(value)

    def insert_after(self, new_val, prev_val):
        node = Node(new_val)
        cur = self.head
        while cur.next:
            if cur.data == prev_val:
                node.next = cur.next
                cur.next = node
                return
            cur = cur.next

    def delete_node_by_val(self, val):
        if self.head is None:
            return
        node = self.head
        if node.data == val:
            self.head = node.next
            node = None
            return
        while node.next:
            tmp = node
            node = node.next
            if node.data == val:
                tmp.next = node.next
                node = None
                return

    def delete_node_by_pos(self, pos):
        node = self.head
        if pos == 0:
            self.head = node.next
            node = None
            return
        i = 0
        while node.next:
            if pos == (i+1):
                tmp = node.next
                node.next = node.next.next
                tmp = None
                return
            node = node.next
            i += 1

    def get_length_rec(self):
        return self.get_length_rec_helper(self.head)

    def get_length_rec_helper(self, node):
        if node:
            return self.get_length_rec_helper(node.next) + 1
        return 0

    def get_length_iter(self):
        node = self.head
        count = 0
        while node:
            count += 1
            node = node.next
        return count

    def add_a_digit(self, val):
        node = self.head
        last_node = None
        while node.next:
            if node.data < 9:
                last_node = node
            node = node.next
        # Add data
        node.data = node.data + val
        if node.data > 9:
            node.data = node.data % 10

            if not last_node:
                self.insert_at_start(1)
                last_node = self.head.next
            while last_node is not node:
                last_node.data = (last_node.data + 1)%10
                last_node = last_node.next




if __name__ == '__main__':
    llist = LinkedList()
    llist.append(3)
    llist.append(4)
    llist.insert_at_start(1)
    llist.insert_after(3.5, 3)
    llist.delete_node_by_val(3)
    llist.traverse()
    print("*******************")
    llist.delete_node_by_pos(2)
    llist.traverse()
    print("*******************")
    print(llist.get_length_rec())
    print(llist.get_length_iter())
    print("*******************ADD**********")
    llist.truncate()
    llist.append(9)
    llist.append(9)
    llist.append(9)
    llist.append(9)
    llist.add_a_digit(6)
    llist.traverse()
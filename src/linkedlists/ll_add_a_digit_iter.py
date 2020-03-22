# https://www.geeksforgeeks.org/add-the-given-digit-to-a-number-stored-in-a-linked-list/

from src.linkedlists.linked_list_ops import LinkedList


class AddDigit(LinkedList):
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
                last_node.data = (last_node.data + 1) % 10
                last_node = last_node.next


if __name__ == '__main__':
    llist = AddDigit()
    llist.append(9)
    llist.append(9)
    llist.append(9)
    llist.append(9)
    llist.add_a_digit(6)
    llist.traverse()
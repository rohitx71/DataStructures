# https://www.geeksforgeeks.org/add-the-given-digit-to-a-number-stored-in-a-linked-list/

from src.linkedlists.linked_list_ops import LinkedList, Node


class AddDigit(LinkedList):

    def add_a_digit(self, node, val):
        if node.next:
            is_carry = self.add_a_digit(node.next, val)
            if is_carry:
                is_carry = self.is_carry_needed(node)
                if node == self.head:
                    tmp = Node(1)
                    tmp.next = self.head
                    self.head = tmp
                    return
                return is_carry
        else:
            return self.is_carry_needed(node, val)

    def is_carry_needed(self, node, val=1):
        node.data = node.data + val
        if node.data > 9:
            node.data = node.data % 10
            return True


if __name__ == '__main__':
    llist = AddDigit()
    llist.append(9)
    llist.append(9)
    llist.append(9)
    llist.append(9)
    llist.add_a_digit(llist.head, 6)
    llist.traverse()

from src.linkedlists.linked_list_ops import LinkedList


class FindMiddleElement(LinkedList):

    def find_mid(self):
        slow_ptr, fast_ptr = self.head, self.head
        while fast_ptr.next and fast_ptr.next.next:
            fast_ptr = fast_ptr.next.next
            slow_ptr = slow_ptr.next
        return slow_ptr.data


if __name__ == "__main__":
    ll = FindMiddleElement()
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.append(6)
    ll.append(7)
    ll.append(8)
    ll.append(9)
    ll.append(10)
    print(ll.find_mid())
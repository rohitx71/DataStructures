class Node:
    def __init__(self, val, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right


class Tree:
    def in_order(self, node):
        if node:
            self.in_order(node.left)
            print(node.data)
            self.in_order(node.right)

    def insert(self, root, new_val):
        q = list()
        q.append(root)
        while q:
            tmp = q.pop(0)
            if not tmp.left:
                tmp.left = Node(new_val)
                return
            else:
                q.append(tmp.left)

            if not tmp.right:
                tmp.right = Node(new_val)
                return
            else:
                q.append(tmp.right)

    # replace with bottom most right most element
    def delete(self, node):
        if node.right:
            res = self.delete(node.right)
            if not res:
                tmp = node.right
                node.right = None
                return tmp
        if node.left:
            self.delete(node.left)
        return False


if __name__ == "__main__":
    t = Tree()
    n = Node(5)
    n.left = Node(7)
    n.right = Node(6)
    n.left.left = Node(3)
    n.left.right = Node(11)
    t.in_order(n)
    t.insert(n, 9)
    print("Inserted 9")
    t.in_order(n)



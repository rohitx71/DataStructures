"""

"""


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
    def delete(self, root, key):
        if root:
            if not root.left and not root.right:
                if root.key == key:
                    root = None
                    return
            q = list()
            q.append(root)
            key_node, tmp = None, None
            while q:
                tmp = q.pop(0)
                if tmp.data == key:
                    key_node = tmp
                if tmp.left:
                    q.append(tmp.left)
                if tmp.right:
                    q.append(tmp.right)
            if key_node:
                key_node.data = tmp.data
                self.delete_leaf(root, tmp)

    def delete_leaf(self, root, key):
        q = list()
        q.append(root)
        while q:
            tmp = q.pop(0)
            if tmp is key:
                tmp = None
                return
            if tmp.left:
                if tmp.left is key:
                    tmp.left = None
                    return
                q.append(tmp.left)
            if tmp.right:
                if tmp.right is key:
                    tmp.right = None
                    return
                q.append(tmp.right)


if __name__ == "__main__":
    t = Tree()
    root = Node(10)
    root.left = Node(11)
    root.left.left = Node(7)
    root.left.right = Node(12)
    root.right = Node(9)
    root.right.left = Node(15)
    root.right.right = Node(8)
    print("The tree before the deletion:")
    t.in_order(root)
    key = 11
    t.delete(root, key)
    print()
    print("The tree after the deletion;")
    t.in_order(root)


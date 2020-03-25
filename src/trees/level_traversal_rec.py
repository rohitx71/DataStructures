"""
https://www.geeksforgeeks.org/level-order-tree-traversal/
"""

from src.trees.binary_tree import Node, Tree


class LevelOrderTraversalRecursion:
    def level_traverse(self, root):
        if root is None:
            return
        for i in range(self.height(root)):
            self.print_level(root, i+1)

    def print_level(self, root, level):
        if root:
            if level == 1:
                print(root.data)
            else:
                self.print_level(root.left, level-1)
                self.print_level(root.right, level-1)

    def level_traverse_q(self, root):
        if root:
            q = list()
            q.append(root)
            while q:
                tmp = q.pop(0)
                print(tmp.data)
                if tmp.left:
                    q.append(tmp.left)
                if tmp.right:
                    q.append(tmp.right)

    def height(self, node):
        if node:
            l_height = self.height(node.left)
            r_height = self.height(node.right)

            if l_height > r_height:
                return l_height + 1
            else:
                return r_height + 1
        return 0


if __name__ == "__main__":
    n = Node(5)
    n.left = Node(7)
    n.right = Node(6)
    n.left.left = Node(3)
    n.left.right = Node(11)

    print(LevelOrderTraversalRecursion().height(n))
    print("*****REC****")
    print(LevelOrderTraversalRecursion().level_traverse(n))
    print("*****ITER****")
    print(LevelOrderTraversalRecursion().level_traverse_q(n))


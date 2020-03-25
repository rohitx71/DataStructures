from src.trees.binary_tree import Node


class CheckMirrorImage:

    def check_mirror_image(self, root):
        return self.compare_nodes(root, root)

    def compare_nodes(self, n1, n2):
        if not n1 and not n2:
            return True
        if n1.data == n2.data:
            return self.compare_nodes(n1.left, n2.right) & self.compare_nodes(n1.right, n2.left)
        return False


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(2)
    root.left.left = Node(3)
    root.left.right = Node(4)
    root.right.left = Node(4)
    root.right.right = Node(3)
    c1 = CheckMirrorImage()
    print(c1.check_mirror_image(root))

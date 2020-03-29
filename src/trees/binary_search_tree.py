from src.trees.binary_tree import Node, Tree


class BinarySearchTree:

    def insert(self, node, new_node):
        if node:
            if node.data > new_node.data:
                if node.left:
                    self.insert(node.left, new_node)
                else:
                    node.left = new_node
            else:
                if node.right:
                    self.insert(node.right, new_node)
                else:
                    node.right = new_node

    def search(self, node, val):
        if node:
            if node.data > val:
                return self.search(node.left, val)
            if node.data < val:
                return self.search(node.right, val)
            return node

    def delete(self, node, val):
        if node:
            if val < node.data:
                node.left = self.delete(node.left, val)
            elif val > node.data:
                node.right = self.delete(node.right, val)
            else:
                if not node.left:
                    temp = node.right
                    node = None
                    return temp
                if not node.right:
                    temp = node.left
                    node = None
                    return temp
                temp = self.find_min(node.right)
                node.data = temp.data
                self.delete(node.right, temp.data)
                return node

    def find_min(self, node):
        while node.left:
            node = node.left
        return node

if __name__ == "__main__":
    t = Tree()
    b = BinarySearchTree()
    # Let us create the following BST 
    #      50 
    #    /      \ 
    #   30     70 
    #   / \    / \ 
    #  20 40  60 80 
    r = Node(50)
    b.insert(r, Node(30))
    b.insert(r, Node(20))
    b.insert(r, Node(40))
    b.insert(r, Node(70))
    b.insert(r, Node(60))
    b.insert(r, Node(80))
    t.in_order(r)
    print("*** BST tree inorder ****;")
    print((b.search(r, 50)).data)
    # t.in_order(r)




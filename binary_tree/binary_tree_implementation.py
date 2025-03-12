class Node:
    def __init__(self, value=None):
        self.value = value
        self.right = None
        self.left = None


class Tree:
    def __init__(self):
        self.root = None

    def get_root(self):
        return self.root

    def add(self, value):
        if self.root == None:
            self.root = Node(value)
        else:
            self.__add(value, self.root)

    def __add(self, value, node):
        if value < node.value:
            if node.left is not None:
                self.__add(value, node.left)
            else:
                node.left = Node(value)

        else:
            if node.right is not None:
                self.__add(value, node.right)
            else:
                node.right = Node(value)

    def find(self, value):
        if self.root is not None:
            self.__find(value, self.root)
        else:
            return None

    def __find(self, value, node):
        if node.value == value:
            return node
        elif value < node.value and node.left != None:
            self.__find(value, node.left)
        elif value > node.value and node.right != None:
            self.__find(value, node.right)

    def delete_tree(self):
        self.root = None

    def print_tree(self):
        if self.root is not None:
            self.__print_tree(self.root)

    def __print_tree(self, Node):
        if Node is not None:
            self.__print_tree(Node.left)
            print(Node.value)
            self.__print_tree(Node.right)


tree = Tree()
tree.add(3)
tree.add(4)
tree.add(0)
tree.add(8)
tree.add(2)
tree.print_tree()

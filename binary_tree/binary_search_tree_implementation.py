class Node:
    def __init__(self, value):
        self.value= value
        self.left= None
        self.right=None

    def insert(self,value):
        if self.value==value:
            return False
        elif self.value> value:
            if self.left!=None:
                return self.left.insert(value)
            else:
                self.left=Node(value)
                return True
        else:
            if self.right !=None:
                return self.right.insert(value)
            else:
                self.right= Node(value)
                return True


class Tree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root!=None:
            return


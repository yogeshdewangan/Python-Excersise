class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.root = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.root
        self.root = new_node
        print("Inserted: "+ str(data))

    def pop(self):
        if self.root is None:
            print("Stack is empty")
            return -1
        temp= self.root
        self.root=self.root.next
        popped = temp.data
        print("Popped:" + str(popped))

stack = Stack()
stack.push(10)
stack.push(11)

stack.pop()




# Stack is last in first out

class Stack:

    def __init__(self):
        self.stack_array = list()  # stack Array
        self.max_limit = 3  # array limit
        self.top = 0  # top to track

    def push(self, element):
        if self.top >= self.max_limit:
            print("Stack is full, can not insert: " + str(element))
            return
        self.stack_array.append(element)
        print("Inserted: " + str(element))
        self.top += 1

    def pop(self):
        if self.top <= 0:
            print("Stack is empty")
            return
        item = self.stack_array.pop()
        print("Removed: "+str(item))
        self.top -= 1
        return item

    def size(self):
        return self.top


stack_obj = Stack()
stack_obj.push(1)
stack_obj.push(2)
stack_obj.push(3)
stack_obj.push(4)

print(stack_obj.size())

stack_obj.pop()

print(stack_obj.size())

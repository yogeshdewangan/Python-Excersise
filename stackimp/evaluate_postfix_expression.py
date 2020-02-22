class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

def do_math(operation, opr1, opr2):
    if operation == '*':
        return opr1 * opr2
    elif operation =='+':
        return opr1+opr2
    elif operation =='/':
        return opr1/opr2
    elif operation =='-':
        return opr1-opr2


def postfix_evaluation(expression):
    stack = Stack()
    char_list = expression.split()

    for char in char_list:
        if char in "0123456789":
            stack.push(int(char))
        else:
            opr1 = stack.pop()
            opr2 = stack.pop()
            result = do_math(char, opr1,opr2)
            stack.push(result)
    return stack.pop()

print(postfix_evaluation("1 2 3 * /"))

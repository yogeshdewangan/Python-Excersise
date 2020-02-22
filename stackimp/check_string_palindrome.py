
class Stack:
    def __init__(self):
        self.items=[]

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()


def check_palindrome(input):
    stack = Stack()
    is_palindrome=False
    for char in input:
        stack.push(char)

    for char in input:
        if char == stack.pop():
            is_palindrome= True
        else:
            is_palindrome = False

    return is_palindrome

print(check_palindrome("123214"))
print(check_palindrome("hymyh"))

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []

    def peek(self):
        return self.items[-1]

    def __str__(self):
        return str(self.items)


def symbol_match(top, symbol):
    start_symbols = "({["
    close_symbols = ")}]"
    return start_symbols.index(top) == close_symbols.index(symbol)

def balance_symbol(input):
    print("Input: ", input)
    stack=Stack()
    balanced = False
    for symbol in input:
        if symbol in ["(","{","["]:
            stack.push(symbol)
        else:
            if stack.is_empty():
                balanced= False
            else:
                top_symbol = stack.pop()
                if not symbol_match(top_symbol, symbol):
                    balanced=False
                else:
                    balanced=True

    return balanced

print (balance_symbol("[{()}]"))
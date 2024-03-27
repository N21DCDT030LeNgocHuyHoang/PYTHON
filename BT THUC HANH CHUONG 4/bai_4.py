class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

    def size(self):
        return len(self.items)


def HauTo(bt):
    priority = {'+': 1, '-': 1, '*': 2, '/': 2}

    def precedence(operator):
        return priority[operator] if operator in priority else 0

    operand_stack = Stack()
    operator_stack = Stack()

    tokens = bt.split()

    for token in tokens:
        if token.isdigit():
            operand_stack.push(token)
        elif token in '+-*/':
            while (not operator_stack.is_empty()) and (precedence(token) <= precedence(operator_stack.peek())):
                operand2 = operand_stack.pop()
                operand1 = operand_stack.pop()
                operator = operator_stack.pop()
                expression = operand1 + ' ' + operand2 + ' ' + operator
                operand_stack.push(expression)
            operator_stack.push(token)

    while not operator_stack.is_empty():
        operand2 = operand_stack.pop()
        operand1 = operand_stack.pop()
        operator = operator_stack.pop()
        expression = operand1 + ' ' + operand2 + ' ' + operator
        operand_stack.push(expression)

    return operand_stack.pop()


# Sử dụng
expression = "2 + 3 * 5"
print("Biểu thức hậu tố của '{}' là: {}".format(expression, HauTo(expression)))

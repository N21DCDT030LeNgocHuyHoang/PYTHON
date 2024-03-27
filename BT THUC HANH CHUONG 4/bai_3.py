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


def GiaTri(bt):
    priority = {'+': 1, '-': 1, '*': 2, '/': 2}

    def evaluate(operand1, operand2, operator):
        if operator == '+':
            return operand1 + operand2
        elif operator == '-':
            return operand1 - operand2
        elif operator == '*':
            return operand1 * operand2
        elif operator == '/':
            return operand1 / operand2

    operand_stack = Stack()
    operator_stack = Stack()

    i = 0
    while i < len(bt):
        if bt[i].isdigit():
            operand = 0
            while i < len(bt) and bt[i].isdigit():
                operand = operand * 10 + int(bt[i])
                i += 1
            operand_stack.push(operand)
        elif bt[i] in '+-*/':
            while (not operator_stack.is_empty()) and (priority[bt[i]] <= priority[operator_stack.peek()]):
                operand2 = operand_stack.pop()
                operand1 = operand_stack.pop()
                operator = operator_stack.pop()
                result = evaluate(operand1, operand2, operator)
                operand_stack.push(result)
            operator_stack.push(bt[i])
            i += 1
        elif bt[i] == '(':
            operator_stack.push(bt[i])
            i += 1
        elif bt[i] == ')':
            while operator_stack.peek() != '(':
                operand2 = operand_stack.pop()
                operand1 = operand_stack.pop()
                operator = operator_stack.pop()
                result = evaluate(operand1, operand2, operator)
                operand_stack.push(result)
            operator_stack.pop()  # Remove '('
            i += 1

    while not operator_stack.is_empty():
        operand2 = operand_stack.pop()
        operand1 = operand_stack.pop()
        operator = operator_stack.pop()
        result = evaluate(operand1, operand2, operator)
        operand_stack.push(result)

    return operand_stack.pop()


# Sử dụng
expression = "3 + 4 * ( 5 - 2 ) / 2"
print("Giá trị của biểu thức '{}' là: {}".format(expression, GiaTri(expression)))

class Stack:

    def __init__(self, stack):
        self.stack = stack

    def isEmpty(self):
        if len(self.stack) > 0:
            result = False
        else:
            result = True
        return result

    def push(self, new_element):
        self.stack.append(new_element)

    def pop(self):
        i = len(self.stack) - 1
        result = self.stack[i]
        self.stack.pop(i)
        return result

    def peek(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)


def balance_next(sequence_brackets, stack):
    open_bracket = ('(', '[', '{')
    close_bracket = (')', ']', '}')
    for i in sequence_brackets:
        if i in ('[', '(', '{'):
            stack.push(i)
        elif not(stack.isEmpty()) and (open_bracket.index(stack.peek()) == close_bracket.index(i)):
            stack.pop()
        else:
            stack.push(i)
            break

    if stack.isEmpty():
        result = 'Сбалансированно'
    else:
        result = 'Несбалансированно'
    return result

brackets1 = '[([])((([[[]]])))]{()}'
s = Stack([])


if __name__ == '__main__':
    print(balance_next(brackets1, s))

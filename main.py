

class Stack:  # наша стопка
    def __init__(self):
        self.stack_list = []

    def is_empty(self):  # проверка стека на пустоту
        if not self.stack_list:
            return True
        return False

    def push(self, item):  # добавляет новый элемент на вершину стека
        self.stack_list.append(item)

    def pop(self):  # удаляет верхний элемент стека
        return self.stack_list.pop()

    def peek(self):  # возвращает верхний элемент стека, но не удаляет его
        return self.stack_list[-1]

    def size(self):  # возвращает количество элементов в стеке
        return len(self.stack_list)


def correct_expresions(some_exp):  # проверка сбалансированной последовательности

    open_closed = {'(': ')',
                   '[': ']',
                   '{': '}'}  # шаблоны символов

    for char in some_exp:
        if char in open_closed.keys():
            stack.push(char)
        elif char in open_closed.values():
            if stack.is_empty() or open_closed[stack.pop()] != char:
                return False
    return stack.is_empty()


if __name__ == '__main__':
    stack = Stack()
    expressions = ['(((([{}]))))',
                   '[([])((([[[]]])))]{()}',
                   '{{[()]}}',
                   '}{}',
                   '{{[(])]}}',
                   '[[{())}]']

    for some_exp in expressions:
        print(correct_expresions(some_exp))
